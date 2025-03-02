#Create a Python program that calculates the area of different shapes using polymorphism.

import math

class Shape:

    def area(self): #this gets overridden in each subclass
        return 0
    
class Rectangle(Shape):
    width : float
    height : float

    
    def __init__(self, _width: float, _height: float):
        self.width = _width
        self.height = _height

    def area (self):
        return self.width * self.height
    
class Circle(Shape):
    radius : float

    def __init__(self, _radius: float):
        self.radius = _radius

    def area(self):
        return self.radius ** 2 * math.pi
    
class Triangle(Shape):
    base : float
    height : float

    def __init__(self, _base: float, _height: float):
        self.base = _base
        self.height = _height
    
    def area(self):
        return self.base * self.height * 0.5
    
shapes = [Rectangle(10, 5), Circle(7), Triangle(6, 4)]


for shape in shapes:
        print(f"{shape.__class__.__name__} area: {shape.area()}")