# MARK: 문제 5

# 5.	datetime 모듈을 사용하여 다음을 출력하는 코드를 작성하세요.
# (1) 오늘의 년도, 월, 일
# (2) 현재 일자를 형식에 맞추어 출력 (예: 2022년 08월 18일 요일: Thursday)
# (3) 현재 시각을 형식에 맞추어 출력 (예: 12시 35분 25초)

import datetime

today = datetime.date.today()
print(f"오늘의 년도: {today.year} 월: {today.month} 일: {today.day}")

now = datetime.datetime.now()
formatted_date = now.strftime("%Y년 %m월 %d일 요일: %A")
print(f"현재 일자: {formatted_date}")

formatted_time = now.strftime("%H시 %M분 %S초")
print(f"현재 시각: {formatted_time}")
