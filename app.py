import os
from pathlib import Path

import chromadb
from flask import Flask, jsonify, redirect, render_template, request, session, url_for
from llama_index.core import (
    PromptTemplate,
    Settings,
    StorageContext,
    VectorStoreIndex,
    get_response_synthesizer,
)
from llama_index.core.embeddings import MockEmbedding
from llama_index.core.llms import MockLLM
from llama_index.core.postprocessor import LLMRerank
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.vector_stores.chroma import ChromaVectorStore

app = Flask(__name__)
app.secret_key = (
    os.environ.get("FLASK_SECRET_KEY")
    or os.environ.get("SECRET_KEY")
    or "change-me-in-production"
)

BASE_DIR = Path(__file__).resolve().parent
CHROMA_DB_PATH = BASE_DIR / "chroma_db"

app_config = {
    "model": "models/gemini-3.1-flash-lite-preview",
    "qa_prompt_str": (
        "You are an AI assistant specialized in MAST Data documentation.\n"
        "Context information is below.\n"
        "---------------------\n"
        "{context_str}\n"
        "---------------------\n"
        "Using the context information above and no prior knowledge, answer the query.\n"
        "MANDATORY: Answer the query using ONLY the provided context.\n"
        "If the answer is not contained in the context, say 'I cannot answer this based on the provided MAST documentation.'\n"
        "Otherwise, use the context to answer the query.\n"
        "Query: {query_str}\n"
        "Answer: "
    ),
}


def get_api_key() -> str:
    for key_name in (
        "GOOGLE_API_KEY",
        "GEMINI_API_KEY",
        "GOOGLE_GENAI_API_KEY",
        "API_KEY",
    ):
        value = os.environ.get(key_name, "").strip()
        if value:
            return value
    return ""


def get_public_password() -> str:
    return (
        os.environ.get("public_password", "").strip()
        or os.environ.get("PUBLIC_PASSWORD", "").strip()
    )


def auth_enabled() -> bool:
    return bool(get_public_password())


def is_authenticated() -> bool:
    if not auth_enabled():
        return True
    return bool(session.get("is_authenticated", False))


@app.before_request
def require_password_auth():
    allowed_paths = {"/healthz", "/login"}

    if request.path in allowed_paths or request.path.startswith("/static/"):
        return None

    if not auth_enabled():
        return None

    if not is_authenticated():
        if request.path.startswith("/api/") or request.path.startswith("/chat"):
            return jsonify({"error": "Authentication required."}), 401
        return redirect(url_for("login_route"))

    return None


print("Loading Vector Store...")
try:
    if not get_api_key():
        Settings.embed_model = MockEmbedding(embed_dim=768)
    else:
        Settings.embed_model = GoogleGenAIEmbedding(
            model_name="models/gemini-embedding-001", api_key=get_api_key()
        )

    db = chromadb.PersistentClient(path=str(CHROMA_DB_PATH))
    chroma_collection = db.get_or_create_collection("mast_docs")
    if chroma_collection.count() == 0:
        print(
            "Warning: Chroma collection 'mast_docs' is empty. Run ingest.py to populate the vector store."
        )
        index = None
        raise RuntimeError("Empty vector store")

    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    index = VectorStoreIndex.from_vector_store(
        vector_store,
        storage_context=storage_context,
    )
except Exception as exc:
    print(f"Warning: Failed to load vector store: {exc}")
    index = None


def build_query_engine(api_key: str, model_name: str, prompt_str: str):
    if not api_key:
        Settings.embed_model = MockEmbedding(embed_dim=768)
        Settings.llm = MockLLM(max_tokens=256)
        node_postprocessors = []
    else:
        Settings.llm = GoogleGenAI(model=model_name, temperature=0.7, api_key=api_key)
        Settings.embed_model = GoogleGenAIEmbedding(
            model_name="models/gemini-embedding-001", api_key=api_key
        )
        reranker = LLMRerank(choice_batch_size=5, top_n=3, llm=Settings.llm)
        node_postprocessors = [reranker]

    qa_prompt = PromptTemplate(prompt_str)
    response_synthesizer = get_response_synthesizer(
        response_mode="compact",
        text_qa_template=qa_prompt,
    )

    if not index:
        return None, qa_prompt

    retriever = index.as_retriever(similarity_top_k=15)
    query_engine = RetrieverQueryEngine(
        retriever=retriever,
        response_synthesizer=response_synthesizer,
        node_postprocessors=node_postprocessors,
    )
    return query_engine, qa_prompt


query_engine, qa_prompt = build_query_engine(
    get_api_key(), app_config["model"], app_config["qa_prompt_str"]
)


@app.route("/")
def index_route():
    return render_template("index.html")


@app.route("/healthz")
def healthcheck_route():
    status_code = 200 if index is not None else 503
    return (
        jsonify(
            {
                "status": "ok" if status_code == 200 else "degraded",
                "vector_store_loaded": index is not None,
                "chroma_db_path": str(CHROMA_DB_PATH),
                "auth_enabled": auth_enabled(),
                "has_api_key": bool(get_api_key()),
            }
        ),
        status_code,
    )


@app.route("/login", methods=["GET", "POST"])
def login_route():
    error = None

    if request.method == "POST":
        configured_password = get_public_password()
        if not configured_password:
            error = (
                "Server password is not configured. Set the public_password "
                "environment variable."
            )
            return render_template("login.html", error=error), 500

        if request.is_json:
            data = request.get_json(silent=True) or {}
            submitted_password = data.get("password", "")
        else:
            submitted_password = request.form.get("password", "")

        if submitted_password == configured_password:
            session["is_authenticated"] = True
            if request.is_json:
                return jsonify({"success": True})
            return redirect(url_for("index_route"))

        error = "Invalid password."
        if request.is_json:
            return jsonify({"success": False, "error": error}), 401

    return render_template("login.html", error=error)


@app.route("/logout", methods=["POST"])
def logout_route():
    session.pop("is_authenticated", None)
    return redirect(url_for("login_route"))


@app.route("/api/config", methods=["GET", "POST"])
def config_route():
    global query_engine, qa_prompt, app_config

    if request.method == "GET":
        return jsonify(
            {
                "model": app_config["model"],
                "qa_prompt_str": app_config["qa_prompt_str"],
                "has_api_key": bool(get_api_key()),
            }
        )

    data = request.get_json(silent=True) or {}
    api_key = data.get("api_key", "").strip()
    model = data.get("model", "").strip()
    prompt_str = data.get("qa_prompt_str", "").strip()

    if api_key:
        os.environ["GOOGLE_API_KEY"] = api_key

    if model:
        app_config["model"] = model

    if prompt_str:
        app_config["qa_prompt_str"] = prompt_str

    try:
        query_engine, qa_prompt = build_query_engine(
            get_api_key(), app_config["model"], app_config["qa_prompt_str"]
        )
        return jsonify({"success": True})
    except Exception as exc:
        return jsonify({"success": False, "error": str(exc)}), 400


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    if not query_engine:
        return (
            jsonify(
                {
                    "error": "Query engine not initialized. Please ensure the vector store is loaded."
                }
            ),
            500,
        )

    if not get_api_key():
        return jsonify(
            {
                "response": "Google API key is not configured. Open Settings, add your API key, and click Update.",
                "sources": [],
            }
        )

    try:
        response = query_engine.query(user_message)

        context_str = "\n\n".join(
            n.node.get_content() if hasattr(n, "node") else n.get_content()
            for n in response.source_nodes
        )
        formatted_prompt = qa_prompt.format(
            context_str=context_str, query_str=user_message
        )
        print("qa_prompt (formatted):", formatted_prompt)

        response_text = (
            getattr(response, "response", None) or str(response) or ""
        ).strip()
        if not response_text or response_text == "Empty Response":
            response_text = (
                "I cannot answer this based on the provided MAST documentation."
            )

        sources = set()
        for node in response.source_nodes:
            metadata = node.metadata
            url = metadata.get("source_url")
            if url:
                sources.add(url)

        return jsonify({"response": response_text, "sources": list(sources)})
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
