# MARK: 문제 3
# 문제3) 좌표(1, 2)에 있는 공이 30도 각도로 15 만큼 이동했을 때 좌표를 구하시오.
# - import math #math 라이브러리를 임포트 함.
# - math 의 함수인 radian, sin, cos 함수를 이용
# - 결과 좌표는 소수 둘째자리에서 반올림함.

import math

x1, y1 = 1, 2
angle_degree = 30
distance = 15

angle_radian = math.radians(angle_degree)
move_x = distance * math.cos(angle_radian)
move_y = distance * math.sin(angle_radian)

new_x = round(x1 + move_x, 2)
new_y = round(y1 + move_y, 2)

print(new_x, new_y)
