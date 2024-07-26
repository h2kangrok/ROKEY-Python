# MARK: 문제 12

import math

year = int(input("연도를 입력하세요. : "))
m = int(input("월을 입력하세요. : "))
d = int(input("날짜를 입력하세요. : "))

Y1 = year % 100
Y2 = year // 100

if m == 1 or m == 2:
    m += 12
    Y1 -= 1

weekday = (Y1 + math.floor(Y1 / 4) - 2 * Y2 + math.floor(Y2 / 4) +
           math.floor((13 * (m + 1)) / 5) + d) % 7

# MARK: 토요일이 0번임
days_of_week = ["토요일", "일요일", "월요일", "화요일", "수요일", "목요일", "금요일"]

print("입력한 날짜의 요일은:", days_of_week[weekday])
