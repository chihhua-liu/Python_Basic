# demo20   reduce

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

courseIncome = tuple({'name': c.name, 'income': c.attendee * 8000} for c in courses)
print("--------------------------------")
pprint(courseIncome)
totalIncome = reduce(lambda acc, value: acc + value['income'], courseIncome, 0)
print("reduce--------------------------------")
print(totalIncome)
print(sum(x['income'] for x in courseIncome))
