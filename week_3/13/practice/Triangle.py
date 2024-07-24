class Triangle:
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.x3 = 0
        self.y3 = 0

    def calcArea(self):
        area = abs(self.x1*(self.y2 - self.y3) + self.x2 *
                   (self.y3 - self.y1) + self.x3*(self.y1 - self.y2)) / 2.0
        return area

    def getCoordsInfo(self):
        self.x1 = int(input("x1 좌표값을 정수로 입력하세요: "))
        self.y1 = int(input("y1 좌표값을 정수로 입력하세요: "))
        self.x2 = int(input("x2 좌표값을 정수로 입력하세요: "))
        self.y2 = int(input("y2 좌표값을 정수로 입력하세요: "))
        self.x3 = int(input("x3 좌표값을 정수로 입력하세요: "))
        self.y3 = int(input("y3 좌표값을 정수로 입력하세요: "))
