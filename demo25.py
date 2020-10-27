#demo25
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
print("reduce ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
courseByCategory = reduce(lambda acc, value: {**acc, **{value.field: acc[value.field] + [value.name]}},
                          courses, {'python': [], 'android': []})
print(courseByCategory)

# explain more on line 17
l1 = ['a', 'b'] + ['c']
print(l1)
d1 = {'a': ['apple'], 'b': ['banana']}
d2 = {'c': ['cookie'], 'b': ['banana', 'beef']}
print({**d1, **d2})