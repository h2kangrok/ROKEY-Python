# MARK: 문제 13
# 문제 13번

import math

a = float(input("직선의 a 계수를 입력하세요: "))
b = float(input("직선의 b 계수를 입력하세요: "))
c = float(input("직선의 c 계수를 입력하세요: "))
x0 = float(input("점의 x 좌표를 입력하세요: "))
y0 = float(input("점의 y 좌표를 입력하세요: "))

numerator = abs(a * x0 + b * y0 + c)
denominator = math.sqrt(a ** 2 + b ** 2)
distance = numerator / denominator

if distance < 0:
    distance *= -1

print("직선과 점 사이의 거리:", distance)
