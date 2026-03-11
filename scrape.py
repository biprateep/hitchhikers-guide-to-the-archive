import asyncio
import os
import re
import json
import logging
import pandas as pd
from urllib.parse import urlparse, urljoin, urldefrag
from datetime import datetime
from langchain_text_splitters import MarkdownHeaderTextSplitter
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def crawl_site_to_markdown(base_url, output_folder="scraped_docs"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    index_rows = []
    
    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
    ]
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)

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
        css_selector=".confluence-content, #content, .page-content, [data-testid='content.views.document.base']",
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
            # Title extraction - try multiple sources for Confluence
            if hasattr(result, "metadata") and result.metadata:
                title = result.metadata.get("title", title)
            if title == "MAST Document" and hasattr(result, "html") and result.html:
                soup = BeautifulSoup(result.html, 'html.parser')
                # Confluence title sources
                title_elem = (
                    soup.find("h1", class_="page-title") or
                    soup.find("h1") or
                    soup.find("title")
                )
                if title_elem:
                    title = title_elem.get_text(strip=True)
                
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
                
                if full_url.startswith(base_domain) and full_url not in visited and full_url not in queue and "$" not in full_url:
                    queue.append(full_url)
                    
            # 3. Get clean Markdown, fallback to Confluence content extraction
            md_text = result.markdown
            
            # If markdown is empty, extract from HTML (Confluence-specific)
            if not md_text or not md_text.strip():
                if hasattr(result, "html") and result.html:
                    soup = BeautifulSoup(result.html, 'html.parser')
                    
                    # Try to find Confluence content area
                    content_div = (
                        soup.find(class_="confluence-content") or
                        soup.find(id="content") or
                        soup.find(class_="page-content") or
                        soup.find("article") or
                        soup.find("main")
                    )
                    
                    if not content_div:
                        content_div = soup
                    
                    # Remove unwanted elements common in Confluence
                    for element in content_div.find_all(["script", "style", "nav", "footer", ".sidebar", "aside"]):
                        element.decompose()
                    
                    # Remove Confluence UI elements (breadcrumbs, buttons, etc)
                    for element in content_div.find_all(class_=re.compile(r"(breadcrumb|sidebar|navigation|toc|action|meta|button-group|aui-button)")):
                        element.decompose()
                    
                    # Get text content
                    md_text = content_div.get_text(separator='\n', strip=True)
                
            if not md_text or not md_text.strip():
                logger.warning(f"No content found for {current_url}")
                continue

            # 4. Chunk with LangChain
            md_header_splits = markdown_splitter.split_text(md_text)

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
                f.write(f"content_length: {len(md_text)}\n")
                f.write("---\n\n")

                if md_header_splits:
                    for i, split in enumerate(md_header_splits):
                        f.write(f"<!-- CHUNK {i+1} START -->\n")
                        header_metadata = {k: v for k, v in split.metadata.items() if k.startswith("Header")}
                        if header_metadata:
                            f.write(f"<!-- Metadata: {json.dumps(header_metadata)} -->\n")
                        f.write(split.page_content + "\n\n")
                        f.write(f"<!-- CHUNK {i+1} END -->\n\n")
                else:
                    f.write(md_text)

            index_rows.append({
                "url": current_url,
                "title": title,
                "filepath": filepath,
                "chunks": len(md_header_splits),
                "content_length": len(md_text)
            })
            logger.info(f"Saved {len(md_text)} chars to {filepath}")

    index_path = os.path.join(output_folder, "index.csv")
    df = pd.DataFrame(index_rows)
    df.to_csv(index_path, index=False)
    logger.info(f"Index written: {index_path}")

if __name__ == "__main__":
    target_url = "https://outerspace.stsci.edu/spaces/MASTDOCS/overview"
    asyncio.run(crawl_site_to_markdown(target_url, "scraped_docs"))
