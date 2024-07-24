# MARK: 문제 3

# 3.	입력 데이터를 기반으로 사각형 또는 원의 면적을 계산하는 프로그램을 작성하십시오. 아래 요구사항을 참고하시오.
# 요구사항:
# •	사각형과 원을 별도의 클래스로 구현합니다. 사각형은 "1"에 대응되고 원은 "0"에 대응됩니다.
# •	사각형 클래스는 왼쪽 상단 (x1, y1)과 오른쪽 하단(x2, y2) 좌표를 입력받습니다.
# •	원 클래스는 중심 좌표(x, y)와 반지름을 입력받습니다.
# •	좌표 값은 정수형으로 입력받습니다.
# •	사용자는 모양의 종류를 문자열로 입력하며, 이후에 필요한 좌표 값이나 반지름을 입력합니다.
# •	총 세 번의 모양 데이터를 입력받아 각 모양의 면적을 계산하고 출력합니다.

import math


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def calcArea(self):
        return abs((self.x2 - self.x1) * (self.y1 - self.y2))


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def calcArea(self):
        return self.r ** 2 * math.pi


shapeList = []

for i in range(3):
    s = input("도형 모양을 입력하세요 (1:사각형 0:원): ")
    if s == "1":
        x1 = int(input("왼쪽 상단의 x좌표를 입력: "))
        y1 = int(input("왼쪽 상단의 y좌표를 입력: "))
        x2 = int(input("오른쪽 하단의 x좌표를 입력: "))
        y2 = int(input("오른쪽 하단의 y좌표를 입력: "))
        shapeList.append(Rectangle(x1, y1, x2, y2))
    elif s == "0":
        x = int(input("원의 중심 x 좌표를 입력: "))
        y = int(input("원의 중심 y 좌표를 입력: "))
        r = int(input("원의 반지름을 입력: "))
        shapeList.append(Circle(x, y, r))
for s in shapeList:
    print(f"면적: {s.calcArea()}")
