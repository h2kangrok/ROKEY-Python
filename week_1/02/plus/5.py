# MARK: 문제 5

# 문제5) 변수에 담긴 값을 확인해서 숫자인 경우 모두 더하는 프로그램을 작성하시오
# - 변수: var1 = "123", var2 = "abc", var3 = "456", var4 = 789
# - 아래 함수를 이용하여 합을 구하시오.
# def sum_numbers_in_variables(*args):
# total_sum = 0
# for value in args: #for 반복문
# if isinstance(value, str) and value.isdigit():
# total_sum += int(value)
# return total_sum
# * isinstance(value, str)은 value가 정수(int) 또는 실수(float) 타입인지를 확인합니다.
# * isdigit() 메서드는 문자열이 모두 숫자로 이루어져 있을 때 True를 반환합니다.


dic = {"var1": "123", "var2": "abc", "var3": "456", "var4": 789}


def sum_numbers_in_variables(*args):
    total_sum = 0
    for value in args:
        if isinstance(value, str) and value.isdigit():
            total_sum += int(value)
    return total_sum


values = dic.values()

result = sum_numbers_in_variables(*values)
print(result)
