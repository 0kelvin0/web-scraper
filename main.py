import yaml
from scraper_engine import run_scraper, save_output

def main():
    with open("config.yaml") as f:
        config = yaml.safe_load(f)

    for site in config["sites"]:
        name = site["name"]
        url = site["url"]
        output_format = site.get("output_format", "json")  # default to JSON

        print(f"\n🔍 Scraping: {name} at url {url}")
        data = run_scraper(site)

        save_output(data, site_name=name, output_format=output_format)

if __name__ == "__main__":
    main()