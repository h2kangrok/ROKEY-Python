# MARK: 문제 4

# 4.	문제14를 수정해서 사용자로부터 모양을 문자열로 입력 받은 후,
# 객체를 먼저 생성하고, 객체의 멤버 함수를 이용해서 각 모양에 맞는 정보들을 입력 받도록 한다.

import math


class Rectangle:
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0

    def calcArea(self):
        return abs((self.x2 - self.x1) * (self.y1 - self.y2))

    def getCoordsInfo(self):
        self.x1 = int(input("왼쪽 상단의 x 좌표값을 정수로 입력하세요: "))
        self.y1 = int(input("왼쪽 상단의 y 좌표값을 정수로 입력하세요: "))
        self.x2 = int(input("오른쪽 하단의 x 좌표값을 정수로 입력하세요: "))
        self.y2 = int(input("오른쪽 하단의 y 좌표값을 정수로 입력하세요: "))


class Circle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.r = 0

    def calcArea(self):
        return self.r ** 2 * math.pi

    def getCoordsInfo(self):
        self.x = int(input("원의 중심 x 좌표를 입력: "))
        self.y = int(input("원의 중심 y 좌표를 입력: "))
        self.r = int(input("원의 반지름을 입력: "))


shapeList = []
for i in range(3):
    s = input("도형 모양을 입력하세요 (1:사각형 0:원): ")
    if s == "1":
        rect = Rectangle()
        rect.getCoordsInfo()
        shapeList.append(rect)
    else:
        circle = Circle()
        circle.getCoordsInfo()
        shapeList.append(circle)
for s in shapeList:
    print(f"면적: {s.calcArea()}")
