# MARK: 문제 7
# 문제7) 특정 년도와 월을 입력받아 해당 월의 달력을 출력하는 프로그램을 작성하세요.

# - import calendar #calendar 라이브러리 이용
# - calendar.weekday(year, month, 1) # 입력받은 년도와 월의 1일이 시작하는

import calendar


def month_calendar(year, month):
    calendar.weekday(year, month, 1)
    calendar.monthrange(year, month)[1]
    cal = calendar.monthcalendar(year, month)

    for week in cal:
        week_str = ""
        for day in week:
            if day == 0:
                week_str += "   "
            else:
                week_str += f"{day:3d}"
        print(week_str)


year = int(input("연도를 입력하세요. : "))
month = int(input("월을 입력하세요. :"))

month_calendar(year, month)
