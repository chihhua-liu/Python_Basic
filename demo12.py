# demo12
from pprint import pprint
import collections

course = collections.namedtuple('course', ['name', 'field', 'attendee', 'remote'])
print(type(course))
print(course)

poop = course(name='poop', field='python', attendee=10, remote=False)
bdpy = course(name='bdpy', field='python', attendee=15, remote=True)

courses = [poop, bdpy]
pprint(courses)

del courses[0]
pprint(courses)