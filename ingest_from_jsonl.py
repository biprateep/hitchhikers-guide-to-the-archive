import os
import time
import json
import asyncio
import argparse
import chromadb

from llama_index.core import VectorStoreIndex, StorageContext, Settings
from llama_index.core.schema import TextNode
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.gemini import GeminiEmbedding

from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception_type
from google.api_core.exceptions import ResourceExhausted


# ─── Rate-limited Gemini embedding wrapper ────────────────────────────────────

class RateLimitedGeminiEmbedding(GeminiEmbedding):
    """Wraps GeminiEmbedding with exponential-backoff retries for quota errors."""

    @retry(
        wait=wait_exponential(multiplier=2, min=10, max=60),
        stop=stop_after_attempt(10),
        retry=retry_if_exception_type(ResourceExhausted),
    )
    def _get_text_embeddings(self, texts):
        print(f"  Embedding batch of {len(texts)} texts...")
        time.sleep(2.0)
        return super()._get_text_embeddings(texts)

    @retry(
        wait=wait_exponential(multiplier=2, min=10, max=60),
        stop=stop_after_attempt(10),
        retry=retry_if_exception_type(ResourceExhausted),
    )
    async def _aget_text_embeddings(self, texts):
        print(f"  Async embedding batch of {len(texts)} texts...")
        await asyncio.sleep(2.0)
        return await super()._aget_text_embeddings(texts)


# ─── Global LlamaIndex settings ───────────────────────────────────────────────

Settings.embed_model = RateLimitedGeminiEmbedding(
    model_name="models/gemini-embedding-001",
    embed_batch_size=30,
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
    batch_size: int  = 30,
    max_nodes: int | None = None,
    reset_collection: bool = True,
):
    """
    Full ingestion pipeline:
      1. Load pre-chunked nodes from the JSONL scraper output.
      2. Embed them with Gemini (rate-limited).
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
        batch      = nodes[i : i + batch_size]
        batch_num  = i // batch_size + 1
        print(f"\n[Batch {batch_num}/{total_batches}] nodes {i}–{i + len(batch) - 1}")
        index.insert_nodes(batch)
        if i + batch_size < len(nodes):          # no sleep after the last batch
            print("  Sleeping 2 s to respect quota...")
            time.sleep(2.0)

    print(f"\n{'='*60}")
    print(f" Ingestion complete!")
    print(f"  Nodes embedded : {len(nodes)}")
    print(f"  ChromaDB path  : {persist_dir}")
    print(f"  Collection     : {collection}")
    print(f"{'='*60}\n")


# ─── CLI entry point ──────────────────────────────────────────────────────────

def parse_args():
    parser = argparse.ArgumentParser(
        description="Ingest Confluence JSONL chunks into ChromaDB via Gemini embeddings."
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
        default=30,
        help="Nodes per embedding batch — keep ≤30 for Gemini free tier (default: 30)",
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
    return parser.parse_args()


if __name__ == "__main__":
    if "GOOGLE_API_KEY" not in os.environ:
        print("Error: GOOGLE_API_KEY environment variable is not set.")
        raise SystemExit(1)

    args = parse_args()
    ingest_data(
        jsonl_path       = args.input,
        persist_dir      = args.persist_dir,
        collection       = args.collection,
        batch_size       = args.batch_size,
        max_nodes        = args.max_nodes,
        reset_collection = not args.no_reset,
    )
