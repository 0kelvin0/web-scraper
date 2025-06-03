def parse(response):
    yield {
        'url': response.url,
        'title': response.css('title::text').get()
    }
