import storage
import crawler
import threading

sites = ["spiegel", "yahoo"]
file_name = "ourfile.json"

old_headlines = storage.load_previous_storage(file_name, sites)
current_data = crawler.get_data()
new_data = storage.compare_data(old_headlines, current_data)
if new_data:
    storage.update_storage(file_name, current_data)