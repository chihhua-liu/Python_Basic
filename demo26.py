# demo26

from pprint import pprint
import collections
import time

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

print("-----------------------------------------")
def transform(x):
    print(f"process course:{x.name}")
    time.sleep(3)
    r1 = {'name': x.name, 'revenue': x.attendee * 5000}
    print(f"process done for course:{x.name}")
    return r1
    print("-----------------------------------------")


start = time.time()
result = tuple(map(transform, courses))
end = time.time()
print("-----------------------------------------")

print(f"total time:{end - start:.2f}seconds")
pprint(result)