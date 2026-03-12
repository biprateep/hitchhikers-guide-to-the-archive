import os
import time
import asyncio
import pandas as pd
import chromadb
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext, Settings
from llama_index.core.node_parser import SemanticSplitterNodeParser
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore
from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception_type

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
from llama_index.core.embeddings import MockEmbedding
_use_mock = os.environ.get("USE_MOCK_EMBEDDING", "").lower() in ("1", "true", "yes")
if _use_mock:
    Settings.embed_model = MockEmbedding(embed_dim=768)
else:
    Settings.embed_model = RateLimitedGoogleGenAIEmbedding(
        model_name="models/gemini-embedding-001",
        embed_batch_size=30
    )

Settings.chunk_size = 512
Settings.chunk_overlap = 50

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
    

    print("Parsing documents into nodes using SemanticSplitterNodeParser...")
    parser = SemanticSplitterNodeParser(
        buffer_size=1, breakpoint_percentile_threshold=95, embed_model=Settings.embed_model
    )
    nodes = parser.get_nodes_from_documents(documents)

    
    # Truncating nodes to maximum 60 due to Gemini free tier 15 RPM quota limitations
    nodes = nodes[:60]
    print(f"Extracted and truncated to {len(nodes)} nodes for quick demonstration.")

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
