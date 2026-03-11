# Hitchhiker's Guide to the Archive

This is a RAG AI pipeline for the MAST Archive. It uses the crawl4ai library to crawl the MAST Archive website and extract the content into markdown files. It then uses the llama-index library to index the content and answer questions.

## Installation

```bash
uv sync
```

## Usage

Fetch the archive documentation, convert it to markdown, and save it to the `mast_docs` directory.
```bash
uv run python crawl.py
```