import requests
from bs4 import BeautifulSoup

def scrape(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    books = []
    for book in soup.select("article.product_pod"):
        books.append({
            "title": book.h3.a["title"],
            "price": book.select_one(".price_color").text,
            "rating": book.select_one(".star-rating")["class"][-1],
        })
    return books
