# MARK: 문제 8

# 8.	아래 조건에 맞추어 피보나치 수열의 숫자를 생성하는 이터레이터를 구현하라.
# -	피보나치 수열은 다음과 같은 규칙에 따라 정의되는 수열입니다:
# 	첫 번째 숫자는 0입니다.
# 	두 번째 숫자는 1입니다.
# 	세 번째 숫자부터는 바로 직전의 두 숫자의 합으로 정의됩니다.
# -	FibonacciIterator 클래스는 초기화 메서드 __init__에서 피보나치 수열의 처음 두 숫자를 self.a와 self.b에 초기화합니다.
# -	__next__ 메서드는 현재 피보나치 수(self.a)를 반환하고, 다음 피보나치 수를 계산하여 self.a와 self.b를 업데이트합니다.
# -	수열이 100을 넘어가면 멈춥니다.

class FibonacciIterator:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        current = self.a
        if current > 100:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return current


fib_iter = FibonacciIterator()

for number in fib_iter:
    print(number)
