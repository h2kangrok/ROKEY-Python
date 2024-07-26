# 문제6) 이슬점을 구하는 함수를 구현하고, 사용자로부터 입력 받은 습도와 온도로 이슬점을 구하는 프로그램을 작성하시오.
# 이슬점을 구하는 함수는 습도와 온도를 인자로 전달받고 이슬점을 반환한다.

# 이슬점을 구하는 수식:
#   import math
#   d1 = math.log(humid / 100)
#   d2 = (17.62 * temperature) / (243.12 + temperature)
#   이슬점 = (243.12 * (d1 + d2)) / (17.62 - (d1 + d2))

import math

humid = float(input("습도를 입력하세요. : "))
temperature = float(input("온도를 입력하세요. : "))


def dew_point(humid, temperature):
    d1 = math.log(humid / 100)
    d2 = (17.62 * temperature) / (243.12 + temperature)
    return (243.12 * (d1 + d2)) / (17.62 - (d1 + d2))


print(f"이슬점은 {dew_point(humid, temperature):.2f}입니다.")
