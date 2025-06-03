# 🕷️ Web Scraper Framework (Scrapy + Configurable Sites)

A flexible and modular web scraping framework built using Python, Scrapy, and Splash for JavaScript-rendered sites. Easily configurable via a `config.yaml` file.


---

## ⚙️ Requirements

- Python 3.7+
- Scrapy
- PyYAML

Install with:

```bash
pip install -r requirements.txt
```

## 🧩 Configuration (config.yaml)
Each site to scrape is defined in this YAML file:

```yaml
- name: books
  url: https://books.toscrape.com/
  parser: books
  output: json

- name: quotes
  url: https://quotes.toscrape.com/
  parser: quotes
  output: json

- name: quotes
  url: https://quotes.toscrape.com/js/
  parser: quotes
  output_format: json
  output_filename: quotes.json
  use_splash: true
```
name: Output file will be named output/<name>.<output>

## 🚀 How to Run
```bash
Ensure Splash is running:
docker run -p 8050:8050 scrapinghub/splash

cd webscraper
python run_all.py
```
Output files are saved in the output/ folder.

Each site is run sequentially with isolated settings.

## 🧠 How It Works
run_all.py loads config.yaml

For each site:

Sets up Scrapy settings (e.g., output format and file)

Launches MasterSpider with the site config

Calls the corresponding parser in parsers

## ✏️ Writing a Custom Parser
Each parser module should contain a parse(response) function that returns Scrapy Item objects or dictionaries.

Example (parsers/quotes.py):

```python
def parse(response):
    for quote in response.css("div.quote"):
        yield {
            "text": quote.css("span.text::text").get(),
            "author": quote.css("small.author::text").get(),
            "tags": quote.css("div.tags a.tag::text").getall()
        }
```