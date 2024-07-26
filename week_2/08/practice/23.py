# MARK: 문제 23

# 문제23) 사용자로부터 삼각형의 꼭지점 좌표  를 입력 받고 리스트 를  형태로 구성해서 반환하는 함수를 구현한다.
# 함수에서 반환되는 삼각형 좌표 리스트를 이용해서 삼각형의 면적을 구하는 함수를 구현한다.
# 두 개 함수를 이용해서 사용자로부터 입력받은 삼각형 좌표를 이용해서 면적을 계산하고 화면에 출력하는 프로그램을 작성한다.
# 삼각형 좌표를 이용해서 면적을 구하는 것은 헤론의 공식을 이용한다.

# 헤론의 공식: 삼각형의 세 변의 길이를 각각 a, b, c라고 가정할 때 면적을 구하는 공식

import math


def triangle_area(triangle_vertex_coordinates):
    # 삼각형의 꼭짓점 좌표를 받아서 면적을 계산
    c_list = triangle_vertex_coordinates

    # 세 변의 길이 계산
    a = math.sqrt((c_list[1][0] - c_list[0][0])**2 +
                  (c_list[1][1] - c_list[0][1])**2)
    b = math.sqrt((c_list[2][0] - c_list[1][0])**2 +
                  (c_list[2][1] - c_list[1][1])**2)
    c = math.sqrt((c_list[2][0] - c_list[0][0])**2 +
                  (c_list[2][1] - c_list[0][1])**2)

    # 반둘레 계산
    s = (a + b + c) / 2

    # 면적 계산 (헤론의 공식)
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    print(f"삼각형 면적은: {area:.2f}")  # 소수점 이하 두 자리까지 출력


def main():
    triangle_vertex_coordinates = []

    # 사용자로부터 삼각형의 꼭짓점 좌표 입력 받기
    for _ in range(3):
        while True:
            try:
                coordinate = list(
                    map(float, input("삼각형 꼭지점 좌표를 입력하세요. 예: 3 4 : ").split()))
                if len(coordinate) != 2:
                    raise ValueError
                triangle_vertex_coordinates.append(coordinate)
                break
            except ValueError:
                print("잘못된 입력입니다. 두 개의 숫자를 공백으로 구분하여 입력하세요.")

    # 삼각형 면적 계산 및 출력
    triangle_area(triangle_vertex_coordinates)


main()
