import requests
from bs4 import BeautifulSoup

def get_data():
    urls = {
        "spiegel": "https://www.spiegel.de",
        "yahoo": "https://finance.yahoo.com"
    }

    headers = {"User-Agent": "Mozilla/5.0"}
    headlines1 = crawl(urls["spiegel"], headers)
    headlines2 = crawl(urls["yahoo"], headers)

    new_data = {
        "spiegel": headlines1,
        "yahoo": headlines2
    }
    return new_data


def crawl(url, headers):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    titles = []

    for tag in soup.find_all(["h2", "h3"]):
        text = tag.get_text(strip=True)
        if text:
            titles.append(text)

    return titles


