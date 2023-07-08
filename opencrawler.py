import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import time
import logging
from concurrent.futures import ThreadPoolExecutor

class WebCrawler:
    def __init__(self, start_url, max_depth=3, delay=0, num_threads=5, timeout=60):
        self.start_url = start_url
        self.max_depth = max_depth
        self.delay = delay
        self.visited_urls = set()
        self.num_threads = num_threads
        self.timeout = timeout

    def crawl(self, process_page_func):
        self._crawl_url(self.start_url, 0, process_page_func)

    def _crawl_url(self, url, depth, process_page_func):
        if depth > self.max_depth:
            return

        # Delay before sending a request to be polite
        time.sleep(self.delay)

        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error requesting URL: {url} - {str(e)}")
            return

        html = response.text
        self.visited_urls.add(url)
        logging.info(f"Visited URL: {url}")

        # Call the user-specified function to process the page
        process_page_func(url, html)

        # Find all anchor tags and extract the href attribute
        soup = BeautifulSoup(html, "html.parser")
        links = soup.find_all("a", href=True)
        next_urls = []
        for link in links:
            href = link["href"]
            absolute_url = urljoin(url, href)
            parsed_url = urlparse(absolute_url)

            # Filter out non-http(s) URLs and URLs with fragments
            if parsed_url.scheme in ["http", "https"] and not parsed_url.fragment:
                if absolute_url not in self.visited_urls:
                    next_urls.append(absolute_url)

        # Use multi-threading for crawling next URLs
        with ThreadPoolExecutor(max_workers=self.num_threads) as executor:
            futures = []
            for next_url in next_urls:
                futures.append(executor.submit(self._crawl_url, next_url, depth + 1, process_page_func))
            for future in futures:
                future.result()