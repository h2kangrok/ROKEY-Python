# 문제11) randint()함수를 이용해서 1~6까지의 무작위 숫자를 10개 생성하되, 4이하의 숫자만 화면에 출력한다.
# 무작위로 정수를 생성한 후에 4보다 큰 숫자가 나온 경우 에는, 다시 무작위로 숫자를 생성하도록 한다.
import random


def solution():
    numbers = []

    while len(numbers) < 10:
        num = random.randint(1, 6)
        if num <= 4:
            numbers.append(num)

    print(f"4 이하의 숫자 10개: {' '.join(map(str, numbers))}")


solution()
