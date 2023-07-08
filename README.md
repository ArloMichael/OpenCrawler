# OpenCrawler

A Python module that provides a performant, multi-threaded implementation of a web crawler. It allows you to crawl web pages starting from a specified URL and process each page using a custom-defined function.

## Installation

Clone the GitHub repository to your local machine:

``` console
git clone https://github.com/ArloMichael/OpenCrawler.git
```

## Usage

To use OpenCrawler, follow these steps:

1.  Import the logging module:

``` python
import logging
```

2.  Import the OpenCrawler module:

``` python
from opencrawler import WebCrawler
```

3.  Configure logging for the crawler:

``` python
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
```

4.  Define a function to process the crawled pages:

``` python
def process_page(url, html):
    # Custom logic for processing the page
    # ...
    logging.info(f"Processing page: {url}")
    # ...
```

5.  Create an instance of `WebCrawler` with the desired parameters:

``` python
crawler = WebCrawler(start_url="http://example.com", max_depth=2, delay=0.5, num_threads=5, timeout=60)
```

6.  Start the crawling process by calling the `crawl` method and passing the `process_page` function:

``` python
crawler.crawl(process_page)
```

7.  OpenCrawler will start crawling the web pages, following links up to the specified maximum depth. The `process_page` function will be called for each page, allowing you to implement your custom logic to extract information or perform any desired actions.

## Example

Here's an example of using OpenCrawler to crawl web pages and print the URLs:

``` python
import logging
from opencrawler import WebCrawler

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Example function to process the page (custom implementation)
def process_page(url, html):     
    # Custom logic for processing the page     
    # ...     
    logging.info(f"Processing page: {url}")     
    # ...  

# Usage example
crawler = WebCrawler(start_url="http://example.com", max_depth=2, delay=0.5, num_threads=5, timeout=60)
crawler.crawl(process_page)
```

In this example, OpenCrawler is used to crawl web pages starting from `http://example.com` with a maximum depth of 2. The `process_page` function is called for each crawled page, where you can implement your custom logic. In this case, the function logs the URL of each processed page.
