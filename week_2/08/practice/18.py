# MARK: 문제 18
# 문제18) 도형 정보를 담고 있는 튜플의 요소들을 이용해서 도형의 면적을 계산해서 출력하는 프로그램 작성.
# - 도형 정보를 담고 있는 튜플의 예시 (“사각형”, 30, 20, “원”, 10)
# <요구사항>
# - 튜플에 있는 도형의 개수는 정해져 있지 않음
# - 원주율은 math.pi 사용 (import math 필요)
# - calcAndPrintArea() 함수는 튜플을 인자로 받고 면적을 계산해서 화면에 출력
# - 튜플 예시: ("사각형", 30, 20, "원", 10, "사각형", 20, 40, "사각형", 10, 10,"원", 20) 사용
# - 출력 예시: 도형_종류, 면적계산시 필요정보, 넓이

import math


def calcAndPrintArea(shapes_tuple):
    i = 0
    while i < len(shapes_tuple):
        shape_type = shapes_tuple[i]
        if shape_type == "사각형":
            width = shapes_tuple[i + 1]
            height = shapes_tuple[i + 2]
            area = width * height
            print(
                f"도형 종류: {shape_type}, 면적 계산시 필요한 정보 -> 가로: {width}, 세로: {height}, 면적: {area}")
            i += 3

        elif shape_type == "원":
            radius = shapes_tuple[i + 1]
            area = math.pi * (radius ** 2)
            print(
                f"도형 종류: {shape_type}, 면적 계산시 필요한 정보 -> 반지름: {radius}, 면적: {area:.2f}")
            i += 2
        else:
            print("알 수 없는 도형입니다.")
            i += 1


calcAndPrintArea(("사각형", 30, 20, "원", 10, "사각형",
                 20, 40, "사각형", 10, 10, "원", 20))
