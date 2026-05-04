import storage
import crawler
import threading
import time
from New_question import notify_user

sites = ["spiegel", "yahoo"]
file_name = "ourfile.json"

counter = 0
condition = threading.Condition()
lock = threading.Lock()
old_headlines = None
current_data = None
def mark_done():
    global counter

    with condition:   
        counter += 1

        if counter == 2:
            condition.notify()   

def get_old_headlines():
    global old_headlines
    old_headlines = storage.load_previous_storage(file_name, sites)
    mark_done()
def get_current_data():
    global current_data
    current_data = crawler.get_data()
    mark_done()

def compare_and_update_data():
    with condition:
        condition.wait()
        new_data = storage.compare_data(old_headlines, current_data)
        if new_data:
            storage.update_storage(file_name, current_data)
    notify_user(new_data)


t1 = threading.Thread(target=get_old_headlines)
t2 = threading.Thread(target=get_current_data)
t3 = threading.Thread(target=compare_and_update_data)

t3.start()
t1.start()
t2.start()

t1.join()
t2.join()
t3.join()
