import math


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def calcArea(self):
        return math.pi * (self.radius ** 2)
