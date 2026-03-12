# requirements: pip install requests beautifulsoup4 html2text langchain-text-splitters tqdm

import requests
import html2text
import json
from tqdm import tqdm
from langchain_text_splitters import RecursiveCharacterTextSplitter

# ─── CONFIG ───────────────────────────────────────────────────────────────────
BASE_URL   = "https://outerspace.stsci.edu"
SPACE_KEY  = "MASTDOCS"
REST_BASE  = f"{BASE_URL}/rest/api"
HEADERS    = {"Accept": "application/json"}
# If authentication is needed (e.g. private spaces):
# HEADERS["Authorization"] = "Basic <base64(user:token)>"
# ──────────────────────────────────────────────────────────────────────────────


def get_all_pages(space_key: str, limit: int = 500) -> list[dict]:
    """
    Fetch ALL pages in a Confluence space using the REST API with pagination.
    Returns list of page metadata dicts.
    """
    pages = []
    start = 0

    while True:
        url = f"{REST_BASE}/space/{space_key}/content/page"
        params = {
            "limit": limit,
            "start": start,
            "expand": "ancestors,metadata.labels",
        }
        resp = requests.get(url, headers=HEADERS, params=params)
        resp.raise_for_status()
        data = resp.json()

        results = data.get("results", [])
        pages.extend(results)

        # Pagination: stop when we've consumed all results
        if start + limit >= data["size"]:
            break
        start += limit

    print(f"Found {len(pages)} pages in space '{space_key}'")
    return pages


def get_page_content(page_id: str) -> dict:
    """
    Fetch full page content (body + metadata) for a single page.
    'body.view' returns rendered HTML — cleaner than 'body.storage' (raw wiki markup).
    """
    url = f"{REST_BASE}/content/{page_id}"
    params = {
        "expand": "body.view,ancestors,metadata.labels,version",
    }
    resp = requests.get(url, headers=HEADERS, params=params)
    resp.raise_for_status()
    return resp.json()


def html_to_markdown(html: str) -> str:
    """Convert Confluence-rendered HTML to clean Markdown text."""
    converter = html2text.HTML2Text()
    converter.ignore_links      = False  # keep links for context
    converter.ignore_images     = True   # skip image tags
    converter.ignore_tables     = False  # preserve tables as text
    converter.body_width        = 0      # no line wrapping
    converter.unicode_snob      = True
    return converter.handle(html).strip()


def build_page_document(page: dict) -> dict:
    """
    Combine page metadata + cleaned text into a RAG-ready document dict.
    """
    page_id    = page["id"]
    title      = page["title"]
    url        = f"{BASE_URL}/display/{SPACE_KEY}/{title.replace(' ', '+')}"
    ancestors  = [a["title"] for a in page.get("ancestors", [])]
    labels     = [l["name"] for l in page.get("metadata", {})
                                          .get("labels", {})
                                          .get("results", [])]
    html_body  = page.get("body", {}).get("view", {}).get("value", "")
    text       = html_to_markdown(html_body)

    return {
        "id"        : page_id,
        "title"     : title,
        "url"       : url,
        "ancestors" : ancestors,          # page hierarchy / breadcrumb
        "labels"    : labels,
        "text"      : text,
        "char_count": len(text),
    }


def chunk_document(doc: dict, chunk_size=800, chunk_overlap=100) -> list[dict]:
    """
    Split a document into overlapping chunks suitable for embedding.
    Preserves metadata on every chunk.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    chunks = splitter.split_text(doc["text"])

    return [
        {
            **{k: v for k, v in doc.items() if k != "text"},
            "chunk_index" : i,
            "chunk_total" : len(chunks),
            "text"        : chunk,
            # Prepend title for better embedding context
            "text_with_context": f"[{doc['title']}]\n\n{chunk}",
        }
        for i, chunk in enumerate(chunks)
    ]


def crawl_space_for_rag(space_key: str, output_file: str = "mast_docs_chunks.jsonl"):
    """
    Full pipeline: fetch all pages → clean content → chunk → save as JSONL.
    """
    # 1. Get page list
    pages_meta = get_all_pages(space_key)

    all_chunks = []
    skipped    = 0

    # 2. Fetch full content for each page
    for meta in tqdm(pages_meta, desc="Fetching pages"):
        try:
            page     = get_page_content(meta["id"])
            doc      = build_page_document(page)

            if doc["char_count"] < 50:       # skip empty/stub pages
                skipped += 1
                continue

            chunks   = chunk_document(doc)
            all_chunks.extend(chunks)

        except requests.HTTPError as e:
            print(f"  ⚠ Skipping page {meta['id']} ({meta['title']}): {e}")

    # 3. Save as JSONL (one chunk per line — easy to stream into any vector DB)
    with open(output_file, "w", encoding="utf-8") as f:
        for chunk in all_chunks:
            f.write(json.dumps(chunk, ensure_ascii=False) + "\n")

    print(f"\n✅ Done!")
    print(f"   Pages processed : {len(pages_meta) - skipped}")
    print(f"   Pages skipped   : {skipped}")
    print(f"   Total chunks    : {len(all_chunks)}")
    print(f"   Output file     : {output_file}")


# ── RUN ───────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    crawl_space_for_rag(SPACE_KEY)