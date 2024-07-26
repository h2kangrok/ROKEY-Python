# MARK: 문제 8
def valid_date(year, month, day):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if 12 >= month >= 1:
        if 0 < day <= days_in_month[month-1]:
            return True
    return False


year = int(input("년을 입력하세요: "))
month = int(input("월을 입력하세요: "))
day = int(input("일을 입력하세요: "))

if valid_date(year, month, day):
    print(f"{year}년 {month}월 {day}일은 유효한 날짜입니다.")
else:
    print(f"{year}년 {month}월 {day}일은 유효하지 않은 날짜입니다.")
