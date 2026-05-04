import sys
import requests
from bs4 import BeautifulSoup
import json 



def load_previous_storage(file_name, keys_of_headlines):
    old_json = None

    try:
        with open(file_name, "r", encoding="utf-8") as old:
            old_json = json.load(old)

    except FileNotFoundError:
        print("File not found")

    except json.JSONDecodeError:
        print("File is empty or invalid JSON")

    old_headlines = []
    if old_json:
        for key in keys_of_headlines:
            old_headlines.extend(old_json.get(key, []))
    return old_headlines

def update_storage(file_name, new_data):
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(new_data, f, ensure_ascii=False, indent=4)
    print("Successfully updated the Json")

def compare_data(old_data, current_data):
    new_data = set(current_data) - set(old_data)
    return new_data
