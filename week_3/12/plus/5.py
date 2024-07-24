# MARK: 문제 5

# 5. x, y 좌표를 저장할 수 있는 Point 클래스를 구현해 보시오.
# (1) x, y 좌표를 인자로 전달받아 멤버 변수에 저장하는__init__ 함수를 구현한다.
# (2) Point 클래스의 멤버 변수인 x, y를 변경할 수 있는 setX(x). setY(y) 멤버 함수를 구현한다.
# (3) Point 클래스의 멤버 변수인 x, y를 각각 반환하는 getX() getY( )를 구현한다.

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def getCoordinate(self):
        self.x = int(input("x좌표를 정수로 입력하세요: "))
        self.y = int(input("y좌표를 정수로 입력하세요: "))

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y


# 예제 사용
# point = Point()
Point.getCoordinate()
print(f"Initial point: ({Point.getX()}, {Point.getY()})")

# 좌표 변경
# point.setX(15)
# point.setY(25)
# print(f"Updated point: ({point.getX()}, {point.getY()})")
