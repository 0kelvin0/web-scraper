# run_all.py
import yaml
import json
import os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

with open("config.yaml", "r") as f:
    sites = yaml.safe_load(f)

for site in sites:
    settings = get_project_settings().copy()

    output_file = f"output/{site['name']}.{site['output_format']}"
    feed_format = site["output_format"]
    settings.set("FEEDS", {
        output_file: {"format": feed_format, "overwrite": True}
    })

    # Needed for Splash
    settings.set("SPLASH_URL", "http://localhost:8050")
    settings.set("DOWNLOADER_MIDDLEWARES", {
        'scrapy_splash.SplashCookiesMiddleware': 723,
        'scrapy_splash.SplashMiddleware': 725,
        'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
    })
    settings.set("SPIDER_MIDDLEWARES", {
        'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
    })
    settings.set("DUPEFILTER_CLASS", 'scrapy_splash.SplashAwareDupeFilter')
    settings.set("HTTPCACHE_STORAGE", 'scrapy_splash.SplashAwareFSCacheStorage')

    process = CrawlerProcess(settings)
    process.crawl("master", site_config=json.dumps(site))
process.start()
