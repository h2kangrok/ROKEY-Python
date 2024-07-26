# MARK: 문제 16

# 문제16) shapes.txt 파일에 도형의 모양과 좌표가 순서대로 저장되어 있다.

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


def Square_area(width, height):
    area = width * height
    print(f"사갹형 면적은: {area:.2f}")


def circle_area(radius):
    area = math.pi * (radius ** 2)
    print(f"원 면적은: {area:.2f}")


def main():

    with open("shapes.txt", "r", encoding="utf-8") as f:
        data = [line.strip() for line in f]
        print(data)

    i = 0
    while i < len(data):
        shape_type = data[i]
        if shape_type == "사각형":
            width = abs(float(data[i + 1]))
            height = abs(float(data[i + 3]))
            Square_area(width, height)
            i += 5
        elif shape_type == "삼각형":
            triangle_vertex_coordinates = []

            for j in range(i+1, i+7, 2):
                triangle_vertex_coordinates.append(
                    [float(data[j]), float(data[j + 1])])
            triangle_area(triangle_vertex_coordinates)
            i += 7

        elif shape_type == "원":
            radius = abs(float(data[i + 1]))
            circle_area(radius)
            i += 2
        else:
            print("알 수 없는 도형입니다.")
            i += 1


main()
