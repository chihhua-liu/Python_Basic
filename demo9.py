#demo 9 : immutable (不可改變的)

class Person:
    def __init__(self, age):
        self.age = age


age = 38
print(hex(id(age)))   #0x7fffdba30b40
age = 39
print(hex(id(age)))   #0x7fffdba30b60

p1 = Person(38)
print(hex(id(p1)), hex(id(p1.age)))   # 0x299dd7f7460 0x7fffdba30b40   物件位址一樣，變數不同指的位址不一樣
p1.age = 39
print(hex(id(p1)), hex(id(p1.age)))   # 0x299dd7f7460 0x7fffdba30b60