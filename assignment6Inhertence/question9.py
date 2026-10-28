"""
Question 9: Interface.
Define Shape as interface which forces all subclasses to implement area() method.
Define Circle and Triangle as classes which implement the Shape interface.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


circle = Circle(5)
print("Circle area:", circle.area())

triangle = Triangle(4, 6)
print("Triangle area:", triangle.area())
