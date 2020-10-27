# demo10 mutable (list , dictionary)

from pprint import pprint

courses = [{'name': 'poop', 'field': 'python', 'attendee': 10, 'remote': False},
           {'name': 'bdpy', 'field': 'python', 'attendee': 15, 'remote': True},
           {'name': 'andbiz3', 'field': 'android', 'attendee': 5, 'remote': True}]
pprint(courses)
courses[0]['name'] = 'POOP'
pprint(courses)
courses2 = [{'name': 'poop', 'field': 'python', 'attendee': 10, 'remote': False},
            {'name': 'bdpy', 'field': 'python', 'attendee': 15, 'remote': True},
            {'name': 'andbiz3', 'field': 'android', 'attendeen': 5, 'remote': True}]  # attendeen 寫錯不知道
pprint(courses2)
print('attendee' in courses2[2] and courses2[2]['attendee'])