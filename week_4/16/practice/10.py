# MARK: 문제 10

# 10.	정수 하나를 입력 받아서 소수인지 판별하는 프로그램을 작성하시오
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


num = int(input("정수를 입력하세요: "))

if is_prime(num):
    print(f"{num}는 소수입니다.")
else:
    print(f"{num}는 소수가 아닙니다.")


