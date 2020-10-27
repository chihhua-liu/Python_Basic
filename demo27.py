# demo27 multiprocess

# from pprint import pprint
# import collections
# import multiprocessing
#
# import time
#
# course = collections.namedtuple('course', ['name', 'field', 'attendee', 'remote'])
# # print(type(course))
# # print(course)
#
# poop = course(name='poop', field='python', attendee=10, remote=False)
# bdpy = course(name='bdpy', field='python', attendee=15, remote=True)
# pykt = course(name='pykt', field='python', attendee=9, remote=True)
# andbiz = course(name='andbiz', field='android', attendee=5, remote=True)
# aiocv = course(name='aiocv', field='python', attendee=10, remote=True)
# courses = (poop, bdpy, pykt, andbiz, aiocv)
#
#
# # pprint(courses)
#
#
# def transform(x):
#     print(f"process course:{x.name}")
#     time.sleep(3)
#     r1 = {'name': x.name, 'revenue': x.attendee * 5000}
#     print(f"process done for course:{x.name}")
#     return r1
#
#
# if __name__ == '__main__':
#     pool = multiprocessing.Pool()
#     print(f"now we run with {pool._processes} pool")
#     start = time.time()
#     result = tuple(pool.map(transform, courses))
#     end = time.time()
#     print(f"total time:{end - start:.2f}seconds")
#     pprint(result)
#----------------------------------------------
# demo27'
from pprint import pprint
import collections
import multiprocessing
import os
import time

course = collections.namedtuple('course', ['name', 'field', 'attendee', 'remote'])
# print(type(course))
# print(course)

poop = course(name='poop', field='python', attendee=10, remote=False)
bdpy = course(name='bdpy', field='python', attendee=15, remote=True)
pykt = course(name='pykt', field='python', attendee=9, remote=True)
andbiz = course(name='andbiz', field='android', attendee=5, remote=True)
aiocv = course(name='aiocv', field='python', attendee=10, remote=True)
courses = (poop, bdpy, pykt, andbiz, aiocv)


# pprint(courses)


def transform(x):
    print(f"pid:{os.getpid()} process course:{x.name}")
    time.sleep(3)
    r1 = {'name': x.name, 'revenue': x.attendee * 5000}
    print(f"pid:{os.getpid()} process done for course:{x.name}")
    return r1


if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=3, maxtasksperchild=100)
    print(f"now we run with {pool._processes} pool")
    start = time.time()
    result = tuple(pool.map(transform, courses))
    end = time.time()
    print(f"total time:{end - start:.2f}seconds")
    pprint(result)