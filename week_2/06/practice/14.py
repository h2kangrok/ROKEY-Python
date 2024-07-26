# 문제14) 피보나치 수열을 작성하는 프로그램을 작성하시오.
# - 피보나치 수열: 1 1 2 3 5 8 13 21 34 55 89 ...
# - 1항과 2항은 1
# - 3항 이후부터의 n항은 (n-1)항 + (n-2)항
#          * f(n) = f(n-1) + f(n-2)

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


for i in range(1, 15):
    print(fibonacci(i), end=" ")
