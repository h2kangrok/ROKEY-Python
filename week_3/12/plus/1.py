# MARK: 문제 1
# 1.	생성자에서 사각형의 좌측 상단 좌표 x,y와 너비와 높이 w, h를 초기화 하는 사각형(Rectangle) 클래스의 생성자를 구현하시오.

class Rectangle:
    def __init__(self, x, y, width, height):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
