# MARK: 문제 10
# 10.	문제8에서 이터레이터를 이용하여 피보나치 수열을 생성했었다. 여기서는 제네레이터를 이용해서 피보나치 수열을 구현하라.

def fibonacci_generator():
    a, b = 0, 1
    while a <= 100:
        yield a
        a, b = b, a + b


fib_gen = fibonacci_generator()

for number in fib_gen:
    print(number)
