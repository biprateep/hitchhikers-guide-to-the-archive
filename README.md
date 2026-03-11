# Hitchhiker's Guide to the Archive

A RAG (Retrieval-Augmented Generation) AI pipeline for the [MAST Archive](https://outerspace.stsci.edu/spaces/MASTDOCS/overview). It crawls and scrapes NASA MAST documentation, ingests the content into a vector store, and serves a chatbot that answers questions grounded in the official docs.

## Prerequisites

- **Python** ≥ 3.12
- **[uv](https://docs.astral.sh/uv/)** – fast Python package manager (recommended)

## Package Dependencies

The project depends on the following third-party Python packages:

| Package | Used By | Purpose |
|---|---|---|
| `crawl4ai` (≥ 0.8.0) | `crawl.py`, `scrape.py` | Async web crawling with headless browser support |
| `pandas` (≥ 3.0.1) | `crawl.py`, `scrape.py`, `ingest.py` | CSV index reading / writing |
| `beautifulsoup4` | `scrape.py` | HTML link extraction |
| `langchain-text-splitters` | `scrape.py` | Markdown-aware text chunking |
| `chromadb` | `ingest.py`, `app.py` | Persistent vector database |
| `llama-index-core` | `ingest.py`, `app.py` | Core RAG framework (document loading, indexing, querying) |
| `llama-index-vector-stores-chroma` | `ingest.py`, `app.py` | ChromaDB integration for LlamaIndex |
| `llama-index-embeddings-gemini` | `ingest.py`, `app.py` | Google Gemini embedding models |
| `llama-index-llms-gemini` | `app.py` | Google Gemini LLM for answer generation |
| `flask` | `app.py` | Web server for the chatbot UI |
| `tenacity` | `ingest.py` | Retry with exponential backoff for rate-limited API calls |
| `google-api-core` | `ingest.py` | Google API exception types (`ResourceExhausted`) |

> **Note:** Standard library modules used across the project include `asyncio`, `os`, `re`, `json`, `logging`, `time`, `urllib.parse`, and `datetime`.

## Environment Variables

| Variable | Required By | Description |
|---|---|---|
| `GOOGLE_API_KEY` | `ingest.py`, `app.py` | API key for Google Gemini (embeddings and LLM). Obtain one from [Google AI Studio](https://aistudio.google.com/apikey). |

Set it before running ingestion or the chatbot:

```bash
export GOOGLE_API_KEY="your-api-key-here"
```

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/biprateep/hitchhikers-guide-to-the-archive.git
   cd hitchhikers-guide-to-the-archive
   ```

2. **Install dependencies with uv:**

   ```bash
   uv sync
   ```

   This reads `pyproject.toml` and `uv.lock` to install all pinned dependencies into a virtual environment.

   > If you prefer pip, install the packages listed in the table above manually, e.g.  
   > `pip install crawl4ai pandas beautifulsoup4 langchain-text-splitters chromadb llama-index-core llama-index-vector-stores-chroma llama-index-embeddings-gemini llama-index-llms-gemini flask tenacity google-api-core`

## Usage

The pipeline has three stages: **Scrape → Ingest → Serve**.

### 1. Scrape the MAST documentation

Choose one of the two scrapers:

- **`crawl.py`** – BFS deep-crawl (simpler, uses `crawl4ai` deep-crawl strategies):

  ```bash
  uv run python crawl.py
  ```

- **`scrape.py`** – Custom crawler with markdown chunking and metadata (recommended):

  ```bash
  uv run python scrape.py
  ```

  This writes chunked markdown files into `scraped_docs/` along with an `index.csv` mapping filenames to source URLs.

### 2. Ingest into the vector store

Embed the scraped documents and store them in ChromaDB:

```bash
export GOOGLE_API_KEY="your-api-key-here"
uv run python ingest.py
```

This creates/populates the `chroma_db/` directory with vector embeddings.

### 3. Run the chatbot

Start the Flask web server:

```bash
export GOOGLE_API_KEY="your-api-key-here"
uv run python app.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser to chat with the MAST documentation assistant.

## Project Structure

```
├── app.py           # Flask chatbot server with RAG query engine
├── crawl.py         # BFS web crawler (crawl4ai deep-crawl)
├── scrape.py        # Custom crawler with chunking & metadata
├── ingest.py        # Document ingestion into ChromaDB
├── main.py          # Placeholder entry point
├── templates/
│   └── index.html   # Chatbot web UI
├── pyproject.toml   # Project metadata & dependencies
├── uv.lock          # Locked dependency versions
├── chroma_db/       # Persistent vector store (generated)
├── scraped_docs/    # Scraped markdown files (generated)
└── index.csv        # URL-to-file mapping (generated)
```

## License

See [LICENSE](LICENSE) for details.