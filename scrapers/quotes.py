import requests
from bs4 import BeautifulSoup

def scrape(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    quotes = []
    for quote in soup.select("div.quote"):
        quotes.append({
            "text": quote.select_one("span.text").text,
            "author": quote.select_one("small.author").text,
        })
    return quotes
