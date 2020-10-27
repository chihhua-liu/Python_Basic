# demo22

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
cplus = course(name='cplus', field='c/c++', attendee=20, remote=True)
courses = (poop, bdpy, pykt, andbiz, aiocv, cplus)
pprint(courses)


def reducer(acc, value):
    acc.setdefault(value.field, [])
    acc[value.field].append(value.name)
    return acc