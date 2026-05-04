import threading
import time
import logging

from crawler import fetch_website, URLS ##Will get function fetch_website from CRAWLER part
from parser import PARSERS
from storage import (load_previous_storage, update_storage, compare_data)
FILE_NAME = "headlines.json"

current_headlines = {}
def function_sumthing(site_name, url):

    html = fetch_website(site_name, url)

    if html:
        parser_function = PARSERS[site_name]

        headlines = parser_function(html)

        current_data[site_name] = headlines

        logging.info(
            f"{site_name}: Parsed {len(headlines)} headlines")

    else:
        logging.warning(f"{site_name}: No HTML received")

def notify_user(new_headlines):

    print("New headline...")

    for headline in new_headlines:
        print(f"NEW: {headline}")

    print("This Is the new headline i guess")
    logging.info(
        f"User notified about {len(new_headlines)} new headlines")
    



def main():
    logging.info("Program started")
    old_headlines = load_previous_storage(
        FILE_NAME,
        URLS.keys())


for site_name, url in URLS.items():

        thread = threading.Thread(
            target=crawl_site,
            args=(site_name, url))
        
for thread in threads:
    thread.join()
    thread.start()

