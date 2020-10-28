#demo49

import requests
import random

BASE_URL = "https://ucom2019-d306a.firebaseio.com/%s.json"
for _ in range(10):
    response = requests.post(BASE_URL % 'demo6', json={'buyer_name': 'Mark', 'quantity': random.randint(5, 10)})
    print(response.status_code, response.json())