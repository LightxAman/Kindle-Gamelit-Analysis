# TODO: Implement scraper.py
import requests
from bs4 import BeautifulSoup
from .utils import load_config, wait


def fetch_bestsellers():
    config = load_config()
    headers = {'User-Agent': config['user_agent']}
    url = config['base_url']
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    books = []

    for item in soup.select('.s-result-item'):
        title_tag = item.select_one('h2 a span')
        asin = item.get('data-asin')
        if title_tag and asin:
            books.append({
                'title': title_tag.text.strip(),
                'asin': asin
            })

    return books
