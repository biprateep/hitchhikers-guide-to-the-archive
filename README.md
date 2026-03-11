# Hitchhiker's Guide to the Archive

This is a RAG AI pipeline for the MAST Archive. 

## Installation

```bash
uv sync
```

## Usage

Fetch the archive documentation, convert it to markdown, and save it to the `mast_docs` directory.
```bash
uv run python crawl.py
```