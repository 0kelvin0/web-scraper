import importlib
import json
import csv
import os

def load_parser(parser_name):
    try:
        return importlib.import_module(f"scrapers.{parser_name}")
    except ModuleNotFoundError:
        print(f"⚠️  Parser '{parser_name}' not found. Using 'generic' instead.")
        return importlib.import_module("scrapers.generic")

def run_scraper(site_config):
    url = site_config["url"]
    parser_name = site_config["parser"]
    parser = load_parser(parser_name)
    return parser.scrape(url)

def save_output(data, site_name, output_format="json"):
    print(f"💾 Saving output for {site_name} in {output_format} format...")
    os.makedirs("output", exist_ok=True)
    filename = f"output/{site_name}.{output_format}"

    if output_format == "json":
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    elif output_format == "csv":
        if not data:
            print(f"⚠️ No data to write for {site_name}")
            return
        with open(filename, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

    else:
        print(f"⚠️ Unknown output format '{output_format}' for site '{site_name}'")

    print(f"✅ Saved output to {filename}")
