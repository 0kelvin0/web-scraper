# spiders/master_spider.py
import scrapy
from scrapy_splash import SplashRequest
import importlib

class MasterSpider(scrapy.Spider):
    name = "master"

    def __init__(self, site_config=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        import json
        self.site = json.loads(site_config) if site_config else {}
        self.start_urls = [self.site.get("url")]
        self.parser_module = self.site.get("parser", "generic")
        self.use_splash = self.site.get("splash", False)

    def start_requests(self):
        if self.use_splash:
            yield SplashRequest(
                url=self.start_urls[0],
                callback=self.parse,
                args={'wait': 1},
                endpoint='render.html'
            )
        else:
            yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def parse(self, response):
        try:
            parser = importlib.import_module(f"parsers.{self.parser_module}")
            yield from parser.parse(response)
        except Exception as e:
            self.logger.error(f"Error loading parser '{self.parser_module}': {e}")
