# from pprint import pprint
# import collections
#
# course = collections.namedtuple('course', ['name', 'field', 'attendee', 'remote'])
# print(type(course))
# print(course)
#
# poop = course(name='poop', field='python', attendee=10, remote=False)
# bdpy = course(name='bdpy', field='python', attendee=15, remote=True)
# pykt = course(name='pykt', field='python', attendee=9, remote=True)
# andbiz = course(name='andbiz', field='android', attendee=5, remote=True)
# aiocv = course(name='aiocv', field='python', attendee=10, remote=True)
# courses = (poop, bdpy, pykt, andbiz, aiocv)
# pprint(courses)
#---------------------------------------------------------------------------
#demo14  filter

from pprint import pprint
import collections

course = collections.namedtuple('course', ['name', 'field', 'attendee', 'remote'])
print(type(course))
print(course)

poop = course(name='poop', field='python', attendee=10, remote=False)
bdpy = course(name='bdpy', field='python', attendee=15, remote=True)
pykt = course(name='pykt', field='python', attendee=9, remote=True)
andbiz = course(name='andbiz', field='android', attendee=5, remote=True)
aiocv = course(name='aiocv', field='python', attendee=10, remote=False)
courses = (poop, bdpy, pykt, andbiz, aiocv)
pprint(courses)
print("--------------------------------------------------")
remoteCourses = filter(lambda x: x.remote is True, courses)
print(type(remoteCourses))
pprint([x for x in remoteCourses])        # way 1
# pprint(list(remoteCourses))             # way 2
largeCourses = filter(lambda x: x.attendee >= 10, courses)
print(next(largeCourses))                 # way 3
print(next(largeCourses))
print(next(largeCourses))
#print(next(largeCourses))
