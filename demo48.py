import requests

BASE_URL = "https://ucom2019-d306a.firebaseio.com/%s.json"
response = requests.patch(BASE_URL % 'demo4', json={'3': 'Intel', '4': 'Google', '5': 'Apple Inc.'})
print(response.status_code, response.json())
response = requests.patch(BASE_URL % 'demo5', json={'duration': '35hr', 'instructor': "Mark", "location": 'Taipei'})
print(response.status_code, response.json())