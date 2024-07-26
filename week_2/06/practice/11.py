# 문제11) 정수 한 개를 함수의 매개변수를 통해 입력받고, 윤년인지 확인해서 True 또는 False를 반환하는 함수를 구현하고 이를 검수하는 프로그램을 작성하시오.
# <윤년의 조건>
# - 연도가 4로 나누어지면 윤년
# - 연도가 4로 나누어지면서 100으로 나누어지면 윤년 아님
# - 연도가 400으로 나누어지면 윤년

def checkLeapyear():
    year = int(input("연도를 입력해주세요. : "))

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


print(checkLeapyear())
