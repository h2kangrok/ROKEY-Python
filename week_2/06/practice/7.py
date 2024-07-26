# 문제7) 날짜를 출력하는 함수를 구현한다. 함수는 다음 형태로 동작한다.
# >>> PrinteDate(2022, 8, 1)
# Year: 2022
# Month: August
# Day: 1

# 구현된 함수를 이용해서 2022년 9월 20일과 2023년 3월 3일을 출력하는 프로그램을 작성한다.

def PrinteDate(y, m, d):

    month = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
             7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}

    print(f"Year: {y}")
    print(f"Month: {month[m]}")
    print(f"Day: {d}")


PrinteDate(2022, 9, 20)
PrinteDate(2023, 3, 3)
