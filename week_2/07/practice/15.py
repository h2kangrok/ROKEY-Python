# 문제15) 정수 n을 입력 받고 n이 소수(prime number)인지 아닌지 확인하는 함수를 구현한다.
# 사용자로부터 정수 한 개를 입력 받고 이 함수를 이용해서 소수인지 아닌지 화면에 출력하는 프로그램을 작성한다.

import math

num = int(input("정수 한개를 입력하세요. : "))


def prime_number(num):
    if num <= 1:
        return "소수가 아닙니다."
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return "소수가 아닙니다."
        return "소수입니다."


print(prime_number(num))
