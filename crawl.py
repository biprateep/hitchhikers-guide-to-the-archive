import asyncio
import os
import re
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, BrowserConfig
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy

async def crawl_site_to_markdown(base_url, output_folder="mast_docs"):
    # Create output directory
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 1. Configure Browser
    browser_cfg = BrowserConfig(headless=True, verbose=True)

    # 2. Configure Crawling Strategy (Stay within same domain, 2 levels deep)
    # Adjust max_depth and max_pages based on site size
    bfs_strategy = BFSDeepCrawlStrategy(
        max_depth=2, 
        include_external=False, 
        max_pages=100
    )

    # 3. Configure Run Settings
    run_cfg = CrawlerRunConfig(
        deep_crawl_strategy=bfs_strategy,
        cache_mode="BYPASS"
    )

    async with AsyncWebCrawler(config=browser_cfg) as crawler:
        # arun returns a list of results when using a deep crawl strategy
        results = await crawler.arun(url=base_url, config=run_cfg)

        for i, result in enumerate(results):
            if result.success and result.markdown:
                # Create a safe filename from the URL
                filename = re.sub(r'[^\w\-_\. ]', '_', result.url.replace(base_url, ""))
                if not filename or filename == "_":
                    filename = "index"
                
                filepath = os.path.join(output_folder, f"{filename}.md")
                
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(result.markdown)
                
                print(f"Saved: {result.url} -> {filepath}")

if __name__ == "__main__":
    target_url = "https://outerspace.stsci.edu/spaces/MASTDOCS/overview " # Replace with your target site
    asyncio.run(crawl_site_to_markdown(target_url))
