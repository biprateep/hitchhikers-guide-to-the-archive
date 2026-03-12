import os
import json
import argparse
import chromadb

from llama_index.core import VectorStoreIndex, StorageContext, Settings
from llama_index.core.schema import TextNode
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.ollama import OllamaEmbedding

# ─── Config (override via environment variables) ──────────────────────────────
#
#   OLLAMA_BASE_URL   Ollama server address   (default: http://localhost:11434)
#   OLLAMA_EMBED      Embedding model to use  (default: nomic-embed-text)
#
# Pull the embedding model before running:
#   ollama pull nomic-embed-text      (~274 MB, fast, great quality)
#   ollama pull mxbai-embed-large     (~670 MB, higher quality, slower)
# ──────────────────────────────────────────────────────────────────────────────

OLLAMA_BASE_URL = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_EMBED    = os.environ.get("OLLAMA_EMBED",    "nomic-embed-text")

# ─── Global LlamaIndex settings ───────────────────────────────────────────────

print(f"Configuring Ollama embed: {OLLAMA_EMBED} @ {OLLAMA_BASE_URL}")

Settings.embed_model = OllamaEmbedding(
    model_name = OLLAMA_EMBED,
    base_url   = OLLAMA_BASE_URL,
)


# ─── JSONL loader ─────────────────────────────────────────────────────────────

def load_nodes_from_jsonl(jsonl_path: str, max_nodes: int | None = None) -> list[TextNode]:
    """
    Read the JSONL produced by the Confluence REST API scraper and convert
    each line into a LlamaIndex TextNode.

    Expected fields per line (all produced by the scraper):
        id, title, url, ancestors, labels,
        chunk_index, chunk_total, char_count,
        text, text_with_context
    """
    nodes: list[TextNode] = []

    with open(jsonl_path, "r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue

            record = json.loads(line)

            # ── Use title-prepended text for richer embeddings ──────────────
            embed_text = record.get("text_with_context") or record.get("text", "")

            if not embed_text.strip():
                continue  # skip empty chunks

            # ── Flatten list fields so ChromaDB can store them ──────────────
            ancestors_str = " > ".join(record.get("ancestors", []))
            labels_str    = ", ".join(record.get("labels", []))

            metadata = {
                "page_id"     : str(record.get("id", "")),
                "title"       : record.get("title", ""),
                "source_url"  : record.get("url", ""),
                "ancestors"   : ancestors_str,          # breadcrumb path
                "labels"      : labels_str,
                "chunk_index" : record.get("chunk_index", 0),
                "chunk_total" : record.get("chunk_total", 1),
            }

            node = TextNode(
                text=embed_text,
                metadata=metadata,
                # Use a stable, deterministic ID so re-runs are idempotent
                id_=f"{record['id']}_chunk{record.get('chunk_index', 0)}",
            )
            nodes.append(node)

            if max_nodes and len(nodes) >= max_nodes:
                print(f"  Reached max_nodes limit ({max_nodes}). Stopping early.")
                break

    print(f"Loaded {len(nodes)} nodes from '{jsonl_path}'.")
    return nodes


# ─── Ingestion pipeline ───────────────────────────────────────────────────────

def ingest_data(
    jsonl_path: str  = "mast_docs_chunks.jsonl",
    persist_dir: str = "./chroma_db",
    collection: str  = "mast_docs",
    batch_size: int  = 64,
    max_nodes: int | None = None,
    reset_collection: bool = True,
):
    """
    Full ingestion pipeline:
      1. Load pre-chunked nodes from the JSONL scraper output.
      2. Embed them locally with Ollama (no rate limits).
      3. Persist into ChromaDB.
    """
    # ── 1. Load nodes ─────────────────────────────────────────────────────────
    print(f"\n{'='*60}")
    print(f" Loading nodes from: {jsonl_path}")
    print(f"{'='*60}")
    nodes = load_nodes_from_jsonl(jsonl_path, max_nodes=max_nodes)

    if not nodes:
        print("No nodes found. Exiting.")
        return

    # ── 2. Set up ChromaDB ────────────────────────────────────────────────────
    print(f"\nInitializing ChromaDB at '{persist_dir}' / collection '{collection}'...")
    db = chromadb.PersistentClient(path=persist_dir)

    if reset_collection:
        try:
            db.delete_collection(collection)
            print(f"  Deleted existing collection '{collection}'.")
        except Exception:
            pass  # didn't exist yet

    chroma_collection = db.get_or_create_collection(collection)
    vector_store      = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context   = StorageContext.from_defaults(vector_store=vector_store)

    # ── 3. Create empty index and insert nodes in batches ────────────────────
    print(f"\nEmbedding and inserting {len(nodes)} nodes in batches of {batch_size}...")
    index = VectorStoreIndex.from_vector_store(
        vector_store,
        storage_context=storage_context,
    )

    total_batches = (len(nodes) + batch_size - 1) // batch_size
    for i in range(0, len(nodes), batch_size):
        batch     = nodes[i : i + batch_size]
        batch_num = i // batch_size + 1
        print(f"\n[Batch {batch_num}/{total_batches}] nodes {i}–{i + len(batch) - 1}")
        index.insert_nodes(batch)

    print(f"\n{'='*60}")
    print(f" Ingestion complete!")
    print(f"  Nodes embedded : {len(nodes)}")
    print(f"  ChromaDB path  : {persist_dir}")
    print(f"  Collection     : {collection}")
    print(f"{'='*60}\n")


# ─── CLI entry point ──────────────────────────────────────────────────────────

def parse_args():
    parser = argparse.ArgumentParser(
        description="Ingest Confluence JSONL chunks into ChromaDB via Ollama embeddings."
    )
    parser.add_argument(
        "--input",
        default="mast_docs_chunks.jsonl",
        help="Path to the JSONL file produced by the REST API scraper (default: mast_docs_chunks.jsonl)",
    )
    parser.add_argument(
        "--persist-dir",
        default="./chroma_db",
        help="Directory where ChromaDB will persist data (default: ./chroma_db)",
    )
    parser.add_argument(
        "--collection",
        default="mast_docs",
        help="ChromaDB collection name (default: mast_docs)",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=64,
        help="Nodes per embedding batch — raise for faster ingestion if RAM allows (default: 64)",
    )
    parser.add_argument(
        "--max-nodes",
        type=int,
        default=None,
        help="Cap total nodes ingested — useful for quick tests (default: no limit)",
    )
    parser.add_argument(
        "--no-reset",
        action="store_true",
        help="Keep existing collection data instead of wiping it before ingestion",
    )
    parser.add_argument(
        "--ollama-url",
        default=None,
        help="Ollama base URL — overrides OLLAMA_BASE_URL env var (default: http://localhost:11434)",
    )
    parser.add_argument(
        "--embed-model",
        default=None,
        help="Ollama embedding model — overrides OLLAMA_EMBED env var (default: nomic-embed-text)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    # CLI flags take precedence over env vars; re-configure if overridden
    if args.ollama_url or args.embed_model:
        base_url   = args.ollama_url  or OLLAMA_BASE_URL
        embed_name = args.embed_model or OLLAMA_EMBED
        print(f"Overriding embed model: {embed_name} @ {base_url}")
        Settings.embed_model = OllamaEmbedding(
            model_name = embed_name,
            base_url   = base_url,
        )

    ingest_data(
        jsonl_path       = args.input,
        persist_dir      = args.persist_dir,
        collection       = args.collection,
        batch_size       = args.batch_size,
        max_nodes        = args.max_nodes,
        reset_collection = not args.no_reset,
    )
