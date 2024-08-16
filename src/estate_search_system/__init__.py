import requests as req
from bs4 import BeautifulSoup
from retry import retry


@retry(tries=3, delay=10, backoff=2)
def load_page(url: str) -> BeautifulSoup:
    html = req.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    return soup
