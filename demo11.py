#demo11

import collections      # used tuple like dictionary --> jey and value

course = collections.namedtuple('course', ['name', 'field', 'attendee', 'remote'])
print(type(course))
print(course)

poop = course(name='poop', field='python', attendee=10, remote=False)
print(poop)
print(poop.name, poop.attendee, poop.remote, poop.field)
#poop.name='Poop'