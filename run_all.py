import yaml
import os
from pathlib import Path
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.master_spider import MasterSpider

def load_configs():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

def run_all_sites():
    configs = load_configs()
    Path("output").mkdir(exist_ok=True)

    for site in configs:
        name = site.get("name", "site")
        output_format = site.get("output", "json")
        url = site.get("url")
        parser = site.get("parser", "generic")

        if not url:
            print(f"Skipping site '{name}' - missing URL")
            continue

        # Prepare per-site settings
        settings = get_project_settings().copy()
        settings.set("FEEDS", {
            f"output/{name}.{output_format}": {
                "format": output_format,
                "overwrite": True
            }
        })

        print(f"Running spider for site: {name} -> output/{name}.{output_format}")

        # Run crawler for this site
        process = CrawlerProcess(settings)
        process.crawl(MasterSpider, site_config={
            "name": name,
            "url": url,
            "parser": parser
        })
    process.start()

if __name__ == "__main__":
    run_all_sites()
