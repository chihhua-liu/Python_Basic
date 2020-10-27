# demo16
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


def available(course):
    return course.attendee >= 10


def isRemote(course):
    return course.remote is True


availableRemoteCourse = tuple(filter(isRemote, filter(available, courses)))
pprint(availableRemoteCourse)
availableRemoteCourse2 = tuple(filter(available, filter(isRemote, courses)))
pprint(availableRemoteCourse2)