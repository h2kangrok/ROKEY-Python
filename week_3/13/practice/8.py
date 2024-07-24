# MARK: 문제 8

# 8.	여섯 개 좌표를 입력 받는 삼각형 클래스를 만들고 모듈화 시킨다. (모듈명은 Triangle.py) 이 삼각형 모듈을 사용해서 면적을 구하는 프로그램을 작성한다.
# (프로그램명: TestTriangle.py) 삼각형의 좌표값은 아래 그림과 같이 직각 삼각형으로 입력된다고 가정한다.

import Triangle
t = Triangle.Triangle()
t.getCoordsInfo()
print(f"삼각형의 넓이 : {t.calcArea()}")
