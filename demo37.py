#demo37     #explain   str() repr() format

from datetime import datetime

now = datetime.now()
print(now)
print(str(now))
print(repr(now))    #repr() format
# under python console
# from datetime import datetime
# ... now = datetime.now()
# now
# datetime.datetime(2020, 10, 27, 14, 2, 10, 325050)
print([now])    #repr() format
print((now,))   #repr() format
print((now))
print({now})
print({'k1': now})
print([str(now)])