#demo42
import json

l1 = ['apple', None, 'orange', 'cookie']
r1 = json.dumps(l1)
print(type(l1), type(r1))
print(l1)
print(r1)
r2 = json.loads(r1)
print(type(r2), r2)
d1 = {'name': "BDPY", 'duration': 35, 'location': "Taipei",
      'period': ['Mon', 'Tue', 'Wed', 'Thr', 'Fri']}
r3 = json.dumps(d1)
print(type(r3), r3)
r4 = json.loads(r3)
print(type(r4), r4)
l2 = ['周一', '過年']
r5 = json.dumps(l2)
print(l2, r5)
r6 = json.loads(r5)
print(r6)