import asyncio
import os
import re
import json
import logging
import pandas as pd
from urllib.parse import urlparse, urljoin, urldefrag
from datetime import datetime
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Compiled once at module level; reused for every URL checked during crawling
_JUNK_PATTERNS = [
    re.compile(r'login', re.IGNORECASE),
    re.compile(r'signup', re.IGNORECASE),
    re.compile(r'\?pageId=', re.IGNORECASE),
    re.compile(r'\?focusedCommentId=', re.IGNORECASE),
    re.compile(r'viewpage\.action\?', re.IGNORECASE),
    re.compile(r'user\.action\?', re.IGNORECASE),
    re.compile(r'history', re.IGNORECASE),
    re.compile(r'attachment', re.IGNORECASE),
    re.compile(r'export', re.IGNORECASE),
    re.compile(r'edit', re.IGNORECASE),
    re.compile(r'aboutconfluencepage\.action', re.IGNORECASE),
    re.compile(r'configurerssfeed\.action', re.IGNORECASE),
    re.compile(r'spacedirectory/', re.IGNORECASE),
    re.compile(r'browsepeople\.action', re.IGNORECASE),
    re.compile(r'collector/', re.IGNORECASE),
]

async def crawl_site_to_markdown(base_url, output_folder="scraped_docs"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    index_rows = []
    
    logger.info(f"Starting crawl at {base_url} with max_pages=200")

    queue = [base_url]
    visited = set()
    base_domain = "https://outerspace.stsci.edu/spaces/MASTDOCS/"
    
    max_pages = 2000
    
    # Configure the crawler for headless operation and robustness
    browser_config = BrowserConfig(
        headless=True,
        headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}
    )
    run_config = CrawlerRunConfig(
        word_count_threshold=10,
        exclude_external_links=True,
        css_selector="#main-content, main, .wiki-content",
        magic=True,
    )
    
    async with AsyncWebCrawler(config=browser_config) as crawler:
        while queue and len(visited) < max_pages:
            current_url = queue.pop(0)
            current_url, _ = urldefrag(current_url)
            
            if current_url in visited or "$" in current_url:
                continue
                
            visited.add(current_url)
            logger.info(f"Processing ({len(visited)}/{max_pages}): {current_url}")
            
            try:
                # 1. Fetch clean markdown using Crawl4AI
                result = await crawler.arun(url=current_url, config=run_config)
                if not result.success:
                    logger.error(f"Failed to fetch {current_url}: {result.error_message}")
                    continue
            except Exception as e:
                logger.error(f"Failed to fetch {current_url} via crawl4ai: {e}")
                continue

            # 2. Extract Title and Links
            title = "MAST Document"
            # Title extraction - Crawl4AI sometimes puts title in result.metadata
            if hasattr(result, "metadata") and result.metadata:
                title = result.metadata.get("title", title)
                
            # Enqueue internal links from both crawl4ai and raw HTML
            internal_links = result.links.get("internal", []) if isinstance(result.links, dict) else []
            links_to_process = [link_obj.get("href") for link_obj in internal_links if link_obj.get("href")]
            
            # Extract links from full raw HTML to bypass CSS selector filtering
            if hasattr(result, "html") and result.html:
                soup = BeautifulSoup(result.html, 'html.parser')
                for a_tag in soup.find_all('a', href=True):
                    links_to_process.append(a_tag['href'])
            
            for href in links_to_process:
                full_url = urljoin(current_url, href)
                full_url, _ = urldefrag(full_url)
                
                # Filter out junk URLs (e.g. login pages, history, raw data, attachment views)
                if any(pattern.search(full_url) for pattern in _JUNK_PATTERNS):
                    continue

                if full_url.startswith(base_domain) and full_url not in visited and full_url not in queue and "$" not in full_url:
                    queue.append(full_url)
                    

            # 3. Get clean Markdown
            md_text = result.markdown
            
            if not md_text or not md_text.strip():
                logger.warning(f"No markdown content found for {current_url}")
                continue

            # Clean up junk characters (e.g. excessive newlines, bizarre symbols if any)
            md_text = re.sub(r'\n{3,}', '\n\n', md_text)

            # We are not chunking here anymore, saving entire cleaned page
            # 5. Save to Hierarchical Storage
            parsed_url = urlparse(current_url)
            path_parts = parsed_url.path.strip("/").split("/")
            
            if path_parts:
                leaf_name = path_parts[-1]
                safe_leaf = re.sub(r'[^\w\-_\. ]', '_', leaf_name)
                dir_path = os.path.join(output_folder, *path_parts[:-1])
                filename = f"{safe_leaf}.md"
            else:
                dir_path = output_folder
                filename = "index.md"

            os.makedirs(dir_path, exist_ok=True)
            filepath = os.path.join(dir_path, filename)


            with open(filepath, "w", encoding="utf-8") as f:
                f.write("---\n")
                f.write(f"title: \"{title}\"\n")
                f.write(f"source_url: \"{current_url}\"\n")
                f.write(f"date_accessed: \"{datetime.now().isoformat()}\"\n")
                f.write("---\n\n")
                f.write(md_text)

            # Store relative filepath for better cross-platform compatibility
            rel_filepath = os.path.relpath(filepath, output_folder)
            index_rows.append({
                "url": current_url,
                "title": title,
                "filepath": rel_filepath,
            })
            logger.info(f"Saved data to {filepath}")

    index_path = os.path.join(output_folder, "index.csv")
    df = pd.DataFrame(index_rows)
    df.to_csv(index_path, index=False)
    logger.info(f"Index written: {index_path}")

if __name__ == "__main__":
    target_url = "https://outerspace.stsci.edu/spaces/MASTDOCS/overview"
    asyncio.run(crawl_site_to_markdown(target_url, "scraped_docs"))
