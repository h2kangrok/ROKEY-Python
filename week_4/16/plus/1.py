# MARK: 문제 1
# 1.	최대공약수(GCD: Great Common Divisor)를 구하는 함수를 작성하고,
# 함수를 이용해 리스트에 있는 여러 숫자의 최대공약수를 구하는 프로그램을 작성하시오

from functools import reduce

# 유클리드 호제법을 이용한 두 숫자의 최대공약수를 구하는 함수


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 리스트에 있는 여러 숫자의 최대공약수를 구하는 함수


def list_gcd(numbers):
    return reduce(gcd, numbers)


# 예제 리스트
numbers = [48, 64, 16, 32]

# 리스트의 최대공약수 계산
result = list_gcd(numbers)

print(f"리스트 {numbers}의 최대공약수는 {result}입니다.")
