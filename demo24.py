# demo24 groupby & sorted

# from pprint import pprint
# import collections
# import itertools
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
#
# sortedCourses = sorted(courses, key=lambda x: x.field)
# print("sorted --------------------------------")
# pprint(tuple(sortedCourses))
#
# print("for groupby------")
# for r in itertools.groupby(sortedCourses, lambda x: x.field):
#     print(type(r), r)
#     print(type(r[0]), r[0])
#     print(type(r[1]))
#     pprint(tuple(r[1]))
#
# print("------")
# print("groupby--------------------------------")
# return1 = {c[0]: list(c[1]) for c in itertools.groupby(sortedCourses, lambda x: x.field)}
# pprint(return1)
# pprint([(c[0], list(c[1])) for c in itertools.groupby(sortedCourses, lambda x: x.field)])
# pprint(tuple((c[0], list(c[1])) for c in itertools.groupby(sortedCourses, lambda x: x.field)))
#--------------------------------------------------------------
#demo24''

from pprint import pprint
import collections
import itertools

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

# sortedCourses = sorted(courses, key=lambda x: x.field)
# pprint(tuple(sortedCourses))
sortedCourses = courses
print("----------------------------------------------------")
for r in itertools.groupby(sortedCourses, lambda x: x.field):
    # print(type(r), r)
    print(type(r[0]), r[0])
    # print(type(r[1]))
    pprint(tuple(r[1]))

print("------------------------------------------------------")
return1 = {c[0]: list(c[1]) for c in itertools.groupby(sortedCourses, lambda x: x.field)}
pprint(return1)
pprint([(c[0], list(c[1])) for c in itertools.groupby(sortedCourses, lambda x: x.field)])
pprint(tuple((c[0], list(c[1])) for c in itertools.groupby(sortedCourses, lambda x: x.field)))
