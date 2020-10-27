from pprint import pprint
import collections
from functools import reduce

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


def reducer(acc, value):
    acc[value.field].append(value.name)
    return acc

#coursesByCategory = reduce(reducer, courses, {})
coursesByCategory = reduce(reducer, courses, {'python': [], 'android': []})
pprint(coursesByCategory)