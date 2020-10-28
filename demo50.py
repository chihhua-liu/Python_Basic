# demo50

import requests

BASE_URL = "https://ucom2019-d306a.firebaseio.com/%s.json"

# strings = ['demo1', 'demo2', 'demo3', 'demo4', 'demo5']
# for s in strings:
#     url = BASE_URL % s
#     response = requests.get(url)
#     print(f"[{response.status_code}], [{type(response.json())}], {response.json()}")

url = BASE_URL % 'demo6'
response = requests.get(url)
print(type(response.json()))
allData = response.json()
for k in allData:
    print(k)
for v in allData.values():
    print(v)
total = 0
for v in allData.values():
    total += v['quantity']
print(f"total={total}")
for k, v in allData.items():
    print(f"key={k}, value={v}")