# MARK: 문제 4

# 문제4) 두 점 (1, 2), (4, 6) 사이의 거리를 구하는 공식을 파이썬 코드로 작성하시오.
# - 거리는 소수 둘째 자리에서 반올림하여 출력함.
# - 거리: 5.00 (확인하세요)

import math

x1, y1 = 1, 2
x2, y2 = 4, 6

delta_x = x2 - x1
delta_y = y2 - y1

distance_squared = delta_x**2 + delta_y**2

print(round(math.sqrt(distance_squared), 2))
