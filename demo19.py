# demo19   used generator and list comprehension : change data content

from pprint import pprint
import collections

course = collections.namedtuple('course', ['name', 'field', 'attendee', 'remote'])
print(type(course))
print(course)

poop = course(name='poop', field='python', attendee=10, remote=False)
bdpy = course(name='bdpy', field='python', attendee=15, remote=True)
pykt = course(name='pykt', field='python', attendee=9, remote=True)
andbiz = course(name='andbiz', field='android', attendee=5, remote=True)
aiocv = course(name='aiocv', field='python', attendee=10, remote=True)
courses = (poop, bdpy, pykt, andbiz, aiocv)
pprint(courses)
print("for list---------------------------------")
pprint([{'name': c.name, 'income': c.attendee * 8000} for c in courses])
print("for tuple---------------------------------")
pprint(tuple({'name': c.name, 'income': c.attendee * 8000} for c in courses))
print("map ---------------------------------")
pprint(tuple(map(lambda x: {'name': x.name, 'income': x.attendee * 8000}, courses)))
