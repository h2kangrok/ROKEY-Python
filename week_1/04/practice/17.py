# MARK: 문제 17
# 문제17) 입력된 정수가 소수인지 판별하는 프로그램을 작성해 보세요.


# 소수 판별 함수(2이상의 자연수에 대하여)

import math


def is_prime_number(num):
    if num <= 1:
        return "소수가 아닙니다."
    elif num == 2:
        return "소수가 입니다."
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return "소수가 아닙니다."
        return "소수가 입니다."


num = int(input("정수를 입력하세요. : "))
print(is_prime_number(num))
