#demo43
import requests

URL1 = "https://bugzilla.mozilla.org/rest/bug/35"
response = requests.get(URL1)
print(response.status_code, type(response.content), response.content[:50])
print(type(response.json()))
bugs = response.json()["bugs"]
firstBug = bugs[0]
for k in firstBug:
    print(k)
print(firstBug['summary'])
ccs = firstBug['cc']
for cc in ccs:
    print(cc)