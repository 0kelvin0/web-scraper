# Multi-Site Web Scraper

A modular Python web scraping project that supports scraping multiple sites with custom parsers.  
Easily configurable via `config.yaml` and supports output to JSON or CSV files.

---

## Features

- Supports multiple websites and parsers
- Uses modular scraper scripts (e.g., `books.py`, `quotes.py`)
- Default fallback parser (`generic.py`)
- Output scraped data as JSON or CSV per site config
- Config-driven (YAML) with easy addition of new sites
- Basic error handling and logging

---

## Requirements

- Python 3.7+
- See `requirements.txt` for dependencies

---

## Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo

   Install dependencies:

2. pip install -r requirements.txt

## Usage
Edit config.yaml to add sites, URLs, parser modules, and output format (json or csv).

Run the scraper:

  ```bash
    python main.py
    Scraped data will be saved under the output/ folder, named by site and output type.
  ```


## How to Add a New Site
Create a new parser in scrapers/, e.g., my_site.py with a scrape(url) function that returns a list of dictionaries.

Add the site to config.yaml with:

```yaml
- name: my_site
  url: https://example.com/
  parser: my_site
  output: json
```

Run python main.py to scrape and save output.
