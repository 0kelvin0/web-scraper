def scrape(url):
    """
    Generic fallback scraper that just fetches and prints raw HTML.

    Args:
        url (str): The URL to fetch.

    Returns:
        list: Dummy list with raw HTML or placeholder text.
    """
    import requests
    res = requests.get(url)
    return [{"html": res.text[:500]}]  # Limit to 500 chars
