from scrapy_splash import SplashRequest

def parse(response):
    for quote in response.css("div.quote"):
        yield {
            "text": quote.css("span.text::text").get(),
            "author": quote.css("small.author::text").get(),
            "tags": quote.css("div.tags a.tag::text").getall(),
        }

    next_page = response.css("li.next a::attr(href)").get()
    if next_page:
        yield SplashRequest(
            response.urljoin(next_page),
            callback=parse,
            args={'wait': 2}
        )