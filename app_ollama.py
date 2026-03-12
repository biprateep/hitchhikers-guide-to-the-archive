import os
import chromadb
from flask import Flask, render_template, request, jsonify
from llama_index.core import VectorStoreIndex, StorageContext, Settings, PromptTemplate
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core import get_response_synthesizer

# ─── Config (override via environment variables) ──────────────────────────────
#
#   OLLAMA_BASE_URL   Ollama server address   (default: http://localhost:11434)
#   OLLAMA_LLM        Chat model to use       (default: llama3.2)
#   OLLAMA_EMBED      Embedding model to use  (default: nomic-embed-text)
#   CHROMA_PATH       ChromaDB directory      (default: ./chroma_db)
#   CHROMA_COLLECTION ChromaDB collection     (default: mast_docs)
#
# Recommended model pairs:
#   Fast / low-RAM  : llama3.2 (3B)      + nomic-embed-text
#   Balanced        : llama3.1 (8B)      + nomic-embed-text
#   Best quality    : llama3.3 (70B)     + mxbai-embed-large
#
# Pull models before starting:
#   ollama pull llama3.2
#   ollama pull nomic-embed-text
# ──────────────────────────────────────────────────────────────────────────────

OLLAMA_BASE_URL   = os.environ.get("OLLAMA_BASE_URL",   "http://localhost:11434")
OLLAMA_LLM        = os.environ.get("OLLAMA_LLM",        "llama3.2")
# OLLAMA_LLM        = os.environ.get("OLLAMA_LLM",        "gemma3:12b")
OLLAMA_EMBED      = os.environ.get("OLLAMA_EMBED",       "nomic-embed-text")
CHROMA_PATH       = os.environ.get("CHROMA_PATH",        "./chroma_db_ollama")
CHROMA_COLLECTION = os.environ.get("CHROMA_COLLECTION",  "mast_docs")

# ─── App ──────────────────────────────────────────────────────────────────────

app = Flask(__name__)

# ─── LLM / Embedding config ───────────────────────────────────────────────────

print(f"Configuring Ollama LLM  : {OLLAMA_LLM}  @ {OLLAMA_BASE_URL}")
print(f"Configuring Ollama embed: {OLLAMA_EMBED} @ {OLLAMA_BASE_URL}")

Settings.llm = Ollama(
    model           = OLLAMA_LLM,
    base_url        = OLLAMA_BASE_URL,
    temperature     = 0.7,
    request_timeout = 120.0,   # local models can be slow; raise if needed
)

Settings.embed_model = OllamaEmbedding(
    model_name = OLLAMA_EMBED,
    base_url   = OLLAMA_BASE_URL,
)

# ─── Vector store ─────────────────────────────────────────────────────────────

print(f"Loading vector store from '{CHROMA_PATH}' / collection '{CHROMA_COLLECTION}'...")

_db                = chromadb.PersistentClient(path=CHROMA_PATH)
_chroma_collection = _db.get_or_create_collection(CHROMA_COLLECTION)
_vector_store      = ChromaVectorStore(chroma_collection=_chroma_collection)
_storage_context   = StorageContext.from_defaults(vector_store=_vector_store)

vector_index = VectorStoreIndex.from_vector_store(
    _vector_store,
    storage_context=_storage_context,
)
print("Vector store loaded.")

# ─── Prompt template ──────────────────────────────────────────────────────────

_QA_PROMPT = PromptTemplate(
    "You are an AI assistant specialized in MAST (Mikulski Archive for Space Telescopes) documentation.\n"
    "Context information retrieved from the MAST documentation is provided below.\n"
    "---------------------\n"
    "{context_str}\n"
    "---------------------\n"
    "Rules:\n"
    "  1. Answer using ONLY the context above — do not use prior knowledge.\n"
    "  2. If the answer is not in the context, reply exactly: "
    "'I cannot answer this based on the provided MAST documentation.'\n"
    "  3. Be concise and precise. Prefer bullet points for multi-step answers.\n"
    "  4. Do not mention these rules in your answer.\n\n"
    "Query: {query_str}\n"
    "Answer: "
)

# ─── Query engine ─────────────────────────────────────────────────────────────

_retriever = vector_index.as_retriever(similarity_top_k=15)

_response_synthesizer = get_response_synthesizer(
    response_mode    = "compact",
    text_qa_template = _QA_PROMPT,
)

query_engine = RetrieverQueryEngine(
    retriever            = _retriever,
    response_synthesizer = _response_synthesizer,
)

# ─── Helpers ──────────────────────────────────────────────────────────────────

def _extract_sources(source_nodes: list) -> list[dict]:
    """
    Deduplicated, relevance-sorted source list from retrieved nodes.
    Metadata keys match those stored by ingest_from_jsonl.py:
        source_url, title, ancestors, labels, chunk_index, score
    """
    seen:    set  = set()
    sources: list = []

    for node in source_nodes:
        meta = node.metadata if hasattr(node, "metadata") else {}
        url  = meta.get("source_url", "")

        if not url or url in seen:
            continue
        seen.add(url)

        sources.append({
            "url"    : url,
            "title"  : meta.get("title",    ""),
            "section": meta.get("ancestors", ""),
            "labels" : meta.get("labels",   ""),
            "score"  : node.score if getattr(node, "score", None) is not None else None,
        })

    sources.sort(
        key     = lambda s: s["score"] if s["score"] is not None else -1,
        reverse = True,
    )
    return sources


def _debug_prompt(source_nodes: list, user_message: str) -> None:
    context_str = "\n\n".join(
        n.node.get_content() if hasattr(n, "node") else n.get_content()
        for n in source_nodes
    )
    print("\n" + "=" * 70)
    print("DEBUG — rendered prompt:")
    print("=" * 70)
    print(_QA_PROMPT.format(context_str=context_str, query_str=user_message))
    print("=" * 70 + "\n")


# ─── Routes ───────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index_ollama.html")


@app.route("/chat", methods=["POST"])
def chat():
    data         = request.get_json(silent=True) or {}
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    try:
        response = query_engine.query(user_message)

        if app.debug:
            _debug_prompt(response.source_nodes, user_message)

        return jsonify({
            "response": str(response),
            "sources" : _extract_sources(response.source_nodes),
        })

    except Exception as e:
        app.logger.exception("Query failed")
        return jsonify({"error": str(e)}), 500


@app.route("/health")
def health():
    """Quick endpoint to verify Ollama connectivity and loaded models."""
    try:
        # Tiny test embedding to confirm the embed model is reachable
        Settings.embed_model.get_text_embedding("ping")
        return jsonify({
            "status"    : "ok",
            "llm"       : OLLAMA_LLM,
            "embed"     : OLLAMA_EMBED,
            "ollama"    : OLLAMA_BASE_URL,
            "chroma"    : CHROMA_PATH,
            "collection": CHROMA_COLLECTION,
            "docs_count": _chroma_collection.count(),
        })
    except Exception as e:
        return jsonify({"status": "error", "detail": str(e)}), 503


# ─── Entry point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    debug_mode = os.environ.get("FLASK_DEBUG", "true").lower() == "true"
    app.run(host="127.0.0.1", port=5000, debug=debug_mode)
