import math
from abc import ABC, abstractmethod 

#polymorphism

#Based on the type of data given, it has been given multiple things to do. (Functions or methods can do multiple things based on given inputs)
#I don't quite undewrstand self
"""
print(len("Kiddos"))

print(len([10,20,30]))
"""

class Shape(ABC):
    def __init__(self, x):
        self.x = x
    @abstractmethod
    def area(self):
        return 0

class Square(Shape):
    def area(self):
        return self.x * self.x

class Circle(Shape):
#Why don't we need another init class?
    def area(self):
        return round(math.pi*self.x**2, 2)
    
class Rectangle(Shape):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y
    def area(self):
        return self.x * self.y
    



sqr = Square(4)
circle = Circle(4)
rec = Rectangle(5, 3)
shapes = [Square(4), Circle(4), "This", Rectangle(5, 3)]
for shape in shapes:
    if isinstance(shape, Shape):
        print(shape.area())
