import os
import time
import asyncio
import pandas as pd
import chromadb
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext, Settings
from llama_index.core.node_parser import SentenceSplitter
import re as _re
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore
from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception_type
from llama_index.core.embeddings import MockEmbedding
from google.api_core.exceptions import ResourceExhausted


class RateLimitedGoogleGenAIEmbedding(GoogleGenAIEmbedding):
    @retry(wait=wait_exponential(multiplier=2, min=10, max=60), stop=stop_after_attempt(10), retry=retry_if_exception_type(ResourceExhausted))
    def _get_text_embeddings(self, texts):
        print(f"Embedding batch of size {len(texts)}...")
        time.sleep(2.0)
        return super()._get_text_embeddings(texts)
    
    @retry(wait=wait_exponential(multiplier=2, min=10, max=60), stop=stop_after_attempt(10), retry=retry_if_exception_type(ResourceExhausted))
    async def _aget_text_embeddings(self, texts):
        print(f"Async embedding batch of size {len(texts)}...")
        await asyncio.sleep(2.0)
        return await super()._aget_text_embeddings(texts)

# Configure global settings
_use_mock = os.environ.get("USE_MOCK_EMBEDDING", "").lower() in ("1", "true", "yes")
if _use_mock:
    Settings.embed_model = MockEmbedding(embed_dim=768)
else:
    Settings.embed_model = RateLimitedGoogleGenAIEmbedding(
        model_name="models/gemini-embedding-001",
        embed_batch_size=30
    )

Settings.chunk_size = 1024
Settings.chunk_overlap = 128

# Patterns marking the start of navigation / boilerplate sections
_NAV_MARKERS = [
    "Unable to load page tree",
    "##### Space shortcuts",
    "[Data Use]",
    "Send comments & corrections",
    "Send comments \\& corrections",
]

def clean_document_text(text: str) -> str:
    """Strip YAML frontmatter, duplicated navigation blocks, and footer boilerplate."""
    # Remove YAML frontmatter
    text = _re.sub(r'^---\n.*?\n---\n*', '', text, count=1, flags=_re.DOTALL)

    # Remove navigation / boilerplate blocks line-by-line
    cleaned_lines = []
    skip = False
    for line in text.splitlines():
        # Check if this line starts a junk block
        if any(marker in line for marker in _NAV_MARKERS):
            skip = True
            continue
        # End the skip region when we hit a real heading (actual content resumes)
        if skip and _re.match(r'^#{1,3} ', line):
            skip = False
        if not skip:
            cleaned_lines.append(line)

    text = '\n'.join(cleaned_lines)
    # Collapse excessive blank lines
    text = _re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def ingest_data(docs_dir="scraped_docs", persist_dir="./chroma_db"):
    print(f"Loading markdown files from {docs_dir}...")
    

    # Load index.csv for source attribution
    mapping = {}
    csv_path = os.path.join(docs_dir, "index.csv")
    if os.path.exists(csv_path):
        try:
            df = pd.read_csv(csv_path)
            for _, row in df.iterrows():
                # row['filepath'] is relative to output_folder/docs_dir (e.g., 'index.md' or 'subdir/file.md')
                # We construct the absolute path properly based on docs_dir
                abs_path = os.path.abspath(os.path.join(docs_dir, row['filepath']))
                mapping[abs_path] = row['url']
            print(f"Loaded {len(mapping)} URL mappings from index.csv.")

        except Exception as e:
            print(f"Failed to load index.csv mapping: {e}")

    def file_metadata(filename):
        return {"source_url": mapping.get(os.path.abspath(filename), "Unknown Source")}

    # Load documents. We filter for .md files.
    loader = SimpleDirectoryReader(
        input_dir=docs_dir, 
        recursive=True, 
        required_exts=[".md"],
        file_metadata=file_metadata
    )
    documents = loader.load_data()
    print(f"Loaded {len(documents)} document fragments.")

    # Clean navigation junk from every document
    skipped = 0
    for doc in documents:
        cleaned = clean_document_text(doc.get_content())
        doc.set_content(cleaned)
        if len(cleaned.strip()) < 20:
            skipped += 1
    documents = [d for d in documents if len(d.get_content().strip()) >= 20]
    print(f"After cleaning: {len(documents)} documents ({skipped} too short, discarded).")

    print(f"Initializing ChromaDB at {persist_dir}...")
    db = chromadb.PersistentClient(path=persist_dir)
    try:
        db.delete_collection("mast_docs")
    except Exception:
        pass  # Collection may not exist
    chroma_collection = db.get_or_create_collection("mast_docs")

    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    print("Parsing, chunking, and embedding documents into ChromaDB. This may take a moment...")

    print("Splitting documents into nodes using SentenceSplitter...")
    parser = SentenceSplitter(
        chunk_size=Settings.chunk_size,
        chunk_overlap=Settings.chunk_overlap,
    )
    nodes = parser.get_nodes_from_documents(documents)
    print(f"Extracted {len(nodes)} nodes from {len(documents)} documents.")

    # Create empty index
    index = VectorStoreIndex.from_vector_store(
        vector_store,
        storage_context=storage_context,
    )
    
    print("Embedding and inserting nodes sequentially to strictly respect quota...")
    batch_size = 30
    for i in range(0, len(nodes), batch_size):
        batch = nodes[i:i+batch_size]
        print(f"Inserting batch {i//batch_size + 1} / {(len(nodes)+batch_size-1)//batch_size} (Nodes {i} to {i+len(batch)})...")
        index.insert_nodes(batch)
        print("Sleeping 2 seconds...")
        time.sleep(2.0)

    print("Ingestion complete! Vector store populated.")

if __name__ == "__main__":
    if not _use_mock and "GOOGLE_API_KEY" not in os.environ:
        print("Error: GOOGLE_API_KEY environment variable is missing.")
    else:
        ingest_data()
