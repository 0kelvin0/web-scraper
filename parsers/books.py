def parse(response):
    for book in response.css('article.product_pod'):
        yield {
            'title': book.css('h3 a::attr(title)').get(),
            'price': book.css('p.price_color::text').get(),
        }
