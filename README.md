# Hitchhiker's Guide to the Archive

A RAG (Retrieval-Augmented Generation) AI pipeline for the [MAST Archive](https://outerspace.stsci.edu/spaces/MASTDOCS/overview). It crawls and scrapes NASA MAST documentation, ingests the content into a vector store, and serves a chatbot that answers questions grounded in the official docs.

## Prerequisites

- **Python** ≥ 3.12
- **[uv](https://docs.astral.sh/uv/)** – fast Python package manager (recommended)
- You can work with conda or micromamba, and you can follow the instructions below.

## Package Dependencies

The project depends on the following third-party Python packages:

| Package | Used By | Purpose |
|---|---|---|
| `crawl4ai` (≥ 0.8.0) | `crawl.py`, `scrape.py` | Async web crawling with headless browser support |
| `pandas` (≥ 3.0.1) | `crawl.py`, `scrape.py`, `ingest.py` | CSV index reading / writing |
| `beautifulsoup4` | `scrape.py`, `rest_api_ext.py` | HTML link extraction |
| `html2text` | `rest_api_ext.py` | HTML to Markdown conversion for REST API scraping |
| `requests` | `rest_api_ext.py` | HTTP requests for Confluence REST API |
| `tqdm` | `rest_api_ext.py` | Progress bars for REST API scraping |
| `langchain-text-splitters` | `scrape.py`, `rest_api_ext.py` | Markdown-aware text chunking |
| `chromadb` | `ingest.py`, `app.py`, `ingest_from_jsonl_ollama.py`, `app_ollama.py` | Persistent vector database |
| `llama-index-core` | `ingest.py`, `app.py`, `ingest_from_jsonl_ollama.py`, `app_ollama.py` | Core RAG framework (document loading, indexing, querying) |
| `llama-index-vector-stores-chroma` | `ingest.py`, `app.py`, `ingest_from_jsonl_ollama.py`, `app_ollama.py` | ChromaDB integration for LlamaIndex |
| `llama-index-embeddings-gemini` | `ingest.py`, `app.py` | Google Gemini embedding models (Gemini path) |
| `llama-index-llms-gemini` | `app.py` | Google Gemini LLM for answer generation (Gemini path) |
| `llama-index-embeddings-ollama` | `ingest_from_jsonl_ollama.py`, `app_ollama.py` | Ollama embedding models (Ollama path) |
| `llama-index-llms-ollama` | `app_ollama.py` | Ollama LLM for answer generation (Ollama path) |
| `flask` | `app.py`, `app_ollama.py` | Web server for the chatbot UI |
| `tenacity` | `ingest.py` | Retry with exponential backoff for rate-limited API calls |
| `google-api-core` | `ingest.py` | Google API exception types (`ResourceExhausted`) |

> **Note:** Standard library modules used across the project include `asyncio`, `os`, `re`, `json`, `logging`, `time`, `urllib.parse`, `argparse`, and `datetime`.

## Environment Variables

### Gemini Path (Google Gemini LLM)

| Variable | Required By | Description |
|---|---|---|
| `GOOGLE_API_KEY` | `ingest.py`, `app.py` | API key for Google Gemini (embeddings and LLM). Obtain one from [Google AI Studio](https://aistudio.google.com/apikey). |

Set it before running ingestion or the chatbot:

```bash
export GOOGLE_API_KEY="your-api-key-here"
```

### Ollama Path (Local LLM)

| Variable | Required By | Default | Description |
|---|---|---|---|
| `OLLAMA_BASE_URL` | `ingest_from_jsonl_ollama.py`, `app_ollama.py` | `http://localhost:11434` | Ollama server address |
| `OLLAMA_LLM` | `app_ollama.py` | `llama3.2` | Chat model name to use (e.g., `llama3.1`, `llama3.3`) |
| `OLLAMA_EMBED` | `ingest_from_jsonl_ollama.py`, `app_ollama.py` | `nomic-embed-text` | Embedding model name (e.g., `mxbai-embed-large`) |
| `CHROMA_PATH` | `ingest_from_jsonl_ollama.py`, `app_ollama.py` | `./chroma_db` | ChromaDB directory path |
| `CHROMA_COLLECTION` | `ingest_from_jsonl_ollama.py`, `app_ollama.py` | `mast_docs` | ChromaDB collection name |

To use the Ollama path, first [install Ollama](https://ollama.ai) and pull the required models:

**Embedding model** (choose one):
```bash
ollama pull nomic-embed-text  # ~274 MB — the embedding model (fast & good quality)
# OR
ollama pull mxbai-embed-large # ~670 MB — higher quality but slower
```

**LLM model** (choose one):
```bash
ollama pull llama3.2           # ~2 GB — the LLM (fast, recommended for CPU)
ollama pull llama3.1           # ~8 GB — balanced quality and speed
ollama pull llama3.3           # ~70 GB — best quality (requires GPU)
```

Then start the Ollama server in a separate terminal:

```bash
ollama serve
```

## Installation

> **Note:** This is a fork of [biprateep/hitchhikers-guide-to-the-archive](https://github.com/biprateep/hitchhikers-guide-to-the-archive), the original project by Biprateep.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/PaulaSanchezSaez/hitchhikers-guide-to-the-archive.git
   cd hitchhikers-guide-to-the-archive
   ```

2. **Option 1: Install dependencies with uv:**

   ```bash
   uv sync
   ```

   This reads `pyproject.toml` and `uv.lock` to install all pinned dependencies into a virtual environment.

   > If you prefer pip, install the packages listed in the table above manually, e.g.  
   > `pip install crawl4ai pandas beautifulsoup4 langchain-text-splitters chromadb llama-index-core llama-index-vector-stores-chroma llama-index-embeddings-gemini llama-index-llms-gemini llama-index-embeddings-ollama llama-index-llms-ollama flask tenacity google-api-core html2text requests tqdm`

3. **Option 2: Install dependencies with conda or micromamba:**

   ```bash
   conda create -n <env_name> python=3.12
   ```

   Then:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

The pipeline has three stages: **Scrape → Ingest → Serve**. You can choose between **Google Gemini** (cloud-based LLM) or **Ollama** (local LLM) paths.

### Stage 1: Scrape the MAST Documentation

#### Option A: Web Crawler (Recommended for quick start)

Use `scrape.py` for a custom crawler with markdown chunking and metadata:

```bash
uv run python scrape.py # if you are using uv
```

or

```bash
python scrape.py # if you are using conda or micromamba
```

This writes chunked markdown files into `scraped_docs/` along with an `index.csv` mapping filenames to source URLs.

#### Option B: Confluence REST API

Use `rest_api_ext.py` to scrape using the official Confluence REST API (more reliable for large spaces):

```bash
uv run python rest_api_ext.py # if you are using uv
```

or

```bash
python rest_api_ext.py # if you are using conda or micromamba
```

This produces structured JSONL output (`mast_docs_chunks.jsonl`) with full metadata (page IDs, titles, URLs, ancestors, labels, chunk info).

### Stage 2: Ingest into the Vector Store

Choose the ingestion path matching your LLM choice.

#### Google Gemini Path

```bash
export GOOGLE_API_KEY="your-api-key-here"
uv run python ingest.py # if you are using uv
```

or

```bash
python ingest.py # if you are using conda or micromamba
```

This uses Google Gemini embeddings and creates/populates `chroma_db/` with vector embeddings.

#### Ollama Path

```bash
# Ensure Ollama is running in another terminal: ollama serve
uv run python ingest_from_jsonl_ollama.py # if you are using uv
```

or

```bash
python ingest_from_jsonl_ollama.py # if you are using conda or micromamba
```

This uses local Ollama embeddings to create/populate `chroma_db/`. The script reads from `mast_docs_chunks.jsonl` (produced by `rest_api_ext.py`).

### Stage 3: Run the Chatbot App

Choose the app matching your ingestion path.

#### Google Gemini Path

```bash
export GOOGLE_API_KEY="your-api-key-here"
uv run python app.py # if you use uv
```

or

```bash
python app.py # if you use conda or micromamba
```

#### Ollama Path

```bash
# Ensure Ollama is running in another terminal: ollama serve
uv run python app_ollama.py # if you use uv
```

or

```bash
python app_ollama.py # if you use conda or micromamba
```

### Stage 4: Chat with the Assistant

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser to chat with the MAST documentation assistant.

## Project Structure

```
├── app.py                          # Flask chatbot (Google Gemini path)
├── app_ollama.py                   # Flask chatbot (Ollama path)
├── crawl.py                        # BFS web crawler (crawl4ai deep-crawl)
├── scrape.py                       # Custom crawler with chunking & metadata
├── rest_api_ext.py                 # Confluence REST API scraper (JSONL output)
├── ingest.py                       # Ingest scraped_docs/ → ChromaDB (Gemini embeddings)
├── ingest_from_jsonl.py            # Ingest JSONL → ChromaDB (Gemini embeddings)
├── ingest_from_jsonl_ollama.py     # Ingest JSONL → ChromaDB (Ollama embeddings)
├── templates/
│   └── index.html                  # Chatbot web UI
├── pyproject.toml                  # Project metadata & dependencies
├── uv.lock                         # Locked dependency versions
├── requirements.txt                # Alternative pip requirements
├── chroma_db/                      # Persistent vector store (generated)
├── scraped_docs/                   # Scraped markdown files (generated by scrape.py)
├── index.csv                       # URL-to-file mapping (generated by scrape.py)
└── mast_docs_chunks.jsonl          # Structured document data (generated by rest_api_ext.py)
```

## License

See [LICENSE](LICENSE) for details.