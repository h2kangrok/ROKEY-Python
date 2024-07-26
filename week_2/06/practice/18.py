# 문제18) 재귀함수를 사용해서 팩토리얼을 계산하는 함수를 구현하세요.

def factorial(n):
    if n == 0:
        return 1
    else:

        return n * factorial(n-1)


print(factorial(5))
