import os
import re
import chromadb
from flask import Flask, render_template, request, jsonify
from llama_index.core import VectorStoreIndex, StorageContext, Settings, PromptTemplate
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core.query_engine import CitationQueryEngine
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core import get_response_synthesizer

app = Flask(__name__)

# Verify API key
if "GOOGLE_API_KEY" not in os.environ:
    print("Warning: GOOGLE_API_KEY environment variable is missing. This will crash LLM.")

# Configure LLM and Embedding locally
# Settings.llm = Gemini(model_name="models/gemma-3-27b-it", temperature=0.7)
Settings.llm = Gemini(model_name="models/gemini-2.5-flash")
Settings.embed_model = GeminiEmbedding(model_name="models/gemini-embedding-001")

# Load Vector Store
print("Loading Vector Store...")
db = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = db.get_or_create_collection("mast_docs")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_vector_store(
    vector_store,
    storage_context=storage_context,
)

# Define Custom Prompt
qa_prompt_str = (
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
qa_prompt = PromptTemplate(qa_prompt_str)


# Create retriever from index
retriever = index.as_retriever(similarity_top_k=15)

# Build response synthesizer with your custom prompt
response_synthesizer = get_response_synthesizer(
    response_mode="compact",  # or "tree_summarize" for longer docs
    text_qa_template=qa_prompt,
)

# Assemble the query engine
query_engine = RetrieverQueryEngine(
    retriever=retriever,
    response_synthesizer=response_synthesizer,
)


# Create Query Engine (no reranker - SentenceTransformerRerank has Mac compatibility issues)
# query_engine = CitationQueryEngine.from_args(
#     index,
#     similarity_top_k=5,
# )

@app.route("/")
def index_route():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    
    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    try:
        response = query_engine.query(user_message)

        # DEBUG STATEMENTS
        # Print the formatted prompt (with context and query filled in)
        context_str = "\n\n".join(
            n.node.get_content() if hasattr(n, "node") else n.get_content()
            for n in response.source_nodes
        )
        formatted_prompt = qa_prompt.format(
            context_str=context_str, query_str=user_message
        )
        print("qa_prompt (formatted):", formatted_prompt)

        # Extract source URLs from source nodes' metadata
        sources = set()
        for node in response.source_nodes:
            # print(f"Node: {node}")
            metadata = node.metadata
            url = metadata.get("source_url")
            # print(f"URL: {url}")  # TODO: These urls are not correct, need to fix
            if url:
                sources.add(url)
                
        return jsonify({
            "response": str(response),
            "sources": list(sources)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
