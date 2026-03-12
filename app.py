import os
import chromadb
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from llama_index.core import VectorStoreIndex, StorageContext, Settings, PromptTemplate
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.postprocessor import LLMRerank
from llama_index.core import get_response_synthesizer
from llama_index.core.embeddings import MockEmbedding
from llama_index.core.llms import MockLLM

app = Flask(__name__)
app.secret_key = (
    os.environ.get("FLASK_SECRET_KEY")
    or os.environ.get("SECRET_KEY")
    or "change-me-in-production"
)

# Global state for settings
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


def get_api_key():
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


def get_public_password():
    return (
        os.environ.get("public_password", "").strip()
        or os.environ.get("PUBLIC_PASSWORD", "").strip()
    )


def is_authenticated():
    configured_password = get_public_password()
    return bool(configured_password) and session.get("is_authenticated", False)


@app.before_request
def require_password_auth():
    allowed_paths = {"/login"}

    if request.path in allowed_paths or request.path.startswith("/static/"):
        return None

    if not is_authenticated():
        if request.path.startswith("/api/") or request.path.startswith("/chat"):
            return jsonify({"error": "Authentication required."}), 401
        return redirect(url_for("login_route"))

    return None


# Load Vector Store
print("Loading Vector Store...")
try:
    if not get_api_key():
        Settings.embed_model = MockEmbedding(embed_dim=768)
    else:
        Settings.embed_model = GoogleGenAIEmbedding(
            model_name="models/gemini-embedding-001", api_key=get_api_key()
        )

    db = chromadb.PersistentClient(path="./chroma_db")
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
except Exception as e:
    print(f"Warning: Failed to load vector store: {e}")
    index = None


# Build the query engine dynamically
def build_query_engine(api_key, model_name, prompt_str):
    if not api_key:
        Settings.embed_model = MockEmbedding(embed_dim=768)
        Settings.llm = MockLLM(max_tokens=256)
        node_postprocessors = []
    else:
        # Use provided parameters
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

    if index:
        retriever = index.as_retriever(similarity_top_k=15)

        qe = RetrieverQueryEngine(
            retriever=retriever,
            response_synthesizer=response_synthesizer,
            node_postprocessors=node_postprocessors,
        )
    else:
        qe = None

    return qe, qa_prompt


# Initialize the global query engine
query_engine, qa_prompt = build_query_engine(
    get_api_key(), app_config["model"], app_config["qa_prompt_str"]
)


@app.route("/")
def index_route():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login_route():
    error = None

    if request.method == "POST":
        configured_password = get_public_password()
        if not configured_password:
            error = "Server password is not configured. Set the public_password environment variable."
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
    elif request.method == "POST":
        data = request.json
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
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
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

        # DEBUG STATEMENTS
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
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
