#demo32

import demo31
from demo31 import foo, bar
import demo31 as d31
from demo31 import foo as f, bar as b

print("now it's demo32")
print(demo31.foo(5, 6))
print(demo31.bar(7, 8))

print(foo(9, 10))
print(bar(11, 12))

print(d31.foo(13, 14))
print(d31.bar(15, 16))

print(f(17, 18))
print(b(19, 20))