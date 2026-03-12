import os
import chromadb
from flask import Flask, render_template, request, jsonify
from llama_index.core import VectorStoreIndex, StorageContext, Settings, PromptTemplate
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.postprocessor import LLMRerank
from llama_index.core import get_response_synthesizer
from llama_index.core.embeddings import MockEmbedding
from llama_index.core.llms import MockLLM

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = "dummy"

app = Flask(__name__)

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
    )
}


def get_api_key():
    return os.environ.get("GOOGLE_API_KEY", "dummy")

# Load Vector Store
print("Loading Vector Store...")
try:
    if get_api_key() == "dummy":
        Settings.embed_model = MockEmbedding(embed_dim=768)
    else:
        Settings.embed_model = GoogleGenAIEmbedding(model_name="models/gemini-embedding-001", api_key=get_api_key())

    db = chromadb.PersistentClient(path="./chroma_db")
    chroma_collection = db.get_or_create_collection("mast_docs")
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
    if api_key == "dummy" or not api_key:
        Settings.embed_model = MockEmbedding(embed_dim=768)
        Settings.llm = MockLLM(max_tokens=256)
        node_postprocessors = []
    else:
        # Use provided parameters
        Settings.llm = GoogleGenAI(model=model_name, temperature=0.7, api_key=api_key)
        Settings.embed_model = GoogleGenAIEmbedding(model_name="models/gemini-embedding-001", api_key=api_key)

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
query_engine, qa_prompt = build_query_engine(get_api_key(), app_config["model"], app_config["qa_prompt_str"])


@app.route("/")
def index_route():
    return render_template("index.html")

@app.route("/api/config", methods=["GET", "POST"])
def config_route():
    global query_engine, qa_prompt, app_config
    if request.method == "GET":
        return jsonify({
            "model": app_config["model"],
            "qa_prompt_str": app_config["qa_prompt_str"],
            "has_api_key": get_api_key() != "dummy" and get_api_key() != ""
        })
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
            query_engine, qa_prompt = build_query_engine(get_api_key(), app_config["model"], app_config["qa_prompt_str"])
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
        return jsonify({"error": "Query engine not initialized. Please ensure the vector store is loaded."}), 500

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

        sources = set()
        for node in response.source_nodes:
            metadata = node.metadata
            url = metadata.get("source_url")
            if url:
                sources.add(url)

        return jsonify({"response": str(response), "sources": list(sources)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
