import scrapy
import importlib

class MasterSpider(scrapy.Spider):
    name = "master"

    def __init__(self, site_config=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.site_config = site_config or {}

    def start_requests(self):
        url = self.site_config.get("url")
        if not url:
            self.logger.error("Missing URL in site_config.")
            return

        yield scrapy.Request(
            url=url,
            callback=self.dispatch_parser,
            meta={
                "parser": self.site_config.get("parser", "generic"),
                "site_name": self.site_config.get("name", "site")
            }
        )

    def dispatch_parser(self, response):
        parser_name = response.meta["parser"]
        site_name = response.meta["site_name"]

        parser_module = importlib.import_module(f"webscraper.parsers.{parser_name}")
        result = parser_module.parse(response)

        for r in result:
            if isinstance(r, scrapy.Request):
                r.meta.update(response.meta)
                yield r
            else:
                r["site"] = site_name
                yield r
