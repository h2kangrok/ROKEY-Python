# MARK: 문제 11

# 11.	문제10의 함수를 람다 함수로 변환하여 간단히 만드는게 적합한지 서술하시오


import math


def is_prime(num):
    return lambda n:  n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))


num = int(input("정수를 입력하세요: "))

if is_prime(num):
    print(f"{num}는 소수입니다.")
else:
    print(f"{num}는 소수가 아닙니다.")
