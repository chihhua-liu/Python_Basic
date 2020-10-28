#demo51

import requests
import time

BASE_URL = "https://ucom2019-d306a.firebaseio.com/%s.json"

strings = ['demo1', 'demo2', 'demo3', 'demo4', 'demo5']
for s in strings:
    time.sleep(5)
    url = BASE_URL % s
    response = requests.delete(url)
    print(f"[{response.status_code}]")

url = BASE_URL % 'demo6'
response = requests.get(url)
allData = response.json()
for k in allData:
    print(k)
    deleteUrl = BASE_URL % ('demo6/' + k)
    print(deleteUrl)
    time.sleep(2)
    response = requests.delete(deleteUrl)
    print(f"[{response.status_code}]")