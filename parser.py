from bs4 import BeautifulSoup

def parse_yahoo_finance(html: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    titles = []
    for tag in soup.find_all("h3", class_="clamp"):
        text = tag.get_text(strip=True)
        if text:
            titles.append(text)
    return titles

def parse_spiegel(html: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    titles = []
    for tag in soup.find_all(attrs={"data-target-teaser-el": "topmark"}):
        text = tag.get_text(strip=True)
        if text:
            titles.append(text)
    return titles

PARSERS = {
    "yahoo_finance": parse_yahoo_finance,
    "spiegel":       parse_spiegel,
}