# 🕷️ Web Scraper Framework (Scrapy + Configurable Sites)

This project is a flexible, configuration-driven web scraping framework built using [Scrapy](https://scrapy.org/). It supports multiple websites, custom parsers, and output formats like JSON and CSV — all controlled via a single `config.yaml` file.

---

## ⚙️ Requirements

- Python 3.7+
- Scrapy
- PyYAML

Install with:

```bash
pip install scrapy pyyaml
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
```
name: Output file will be named output/<name>.<output>

## 🚀 How to Run
```bash
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