# demo69   class:  __init__ : 定義初始值 : class 建構時會執行

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


rect1 = Rectangle(2, 3)
print(rect1.calculate_area())
rect2 = Rectangle(4, 6)
print(rect2.calculate_area())