class Car:
    vendor = 'Lexus'
    valid = True
    pass       # 沒回傳值加: pass

print(Car.vendor, Car.valid)

c1 = Car()
c2 = Car()
Car.function = 'Normal'
print(Car.vendor, Car.valid, Car.function)
print("-------------------------------------------")
print(c1.function, c2.function, Car.function)   # 沒有東西是Normal
print("-------------------------------------------")
c1.color = 'RED'     # 可以動態加入
c2.year = 2020       # 可以動態加入
print(c1.color, c1.vendor, c1.valid, c1.function)
print(c2.year, c2.vendor, c2.valid, c2.function)