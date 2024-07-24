class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def calcArea(self):
        width = abs(self.x2 - self.x1)
        height = abs(self.y2 - self.y1)
        return width * height
