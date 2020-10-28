import requests

BASE_URL = "https://ucom2019-d306a.firebaseio.com/%s.json"

response = requests.put(BASE_URL % 'demo1', json='BDPY1027_Mark~~~')
print(response.status_code, response.json())
response = requests.put(BASE_URL % 'demo2', json=100)
print(response.status_code, response.json())
response = requests.put(BASE_URL % 'demo3', json=3.14159)
print(response.status_code, response.json())
response = requests.put(BASE_URL % 'demo4', json=['apple', 'banana', 'cookie', None, None, '蘋果'])
print(response.status_code, response.json())
response = requests.put(BASE_URL % 'demo5', json={'name': 'BDPY', 'duration': 35})
print(response.status_code, response.json())