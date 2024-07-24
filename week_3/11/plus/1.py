# MARK: 문제 1
# 1.	1~20 사이의 숫자 중에서 무작위로 중복되지 않는 숫자 10개를 뽑아서 출력하는 프로그램을 작성하시오.
# -	새로운 무작위 숫자를 생성했을 때 기존에 저장되어 있던 숫자들과 비교해서 중복되지 않는 숫자이면 새로 저장하고,
# 중복된다면 버리고 새로운 숫자를 생성.
# -	10개의 중복되지 않는 숫자들이 생성될 때까지 반복. 즉,무한 반복하면서 10개가 채워지면 반복을 종료해야 함

import random


def generate_unique_numbers():
    unique_numbers = set()

    while len(unique_numbers) < 10:
        number = random.randint(1, 20)
        unique_numbers.add(number)

    return unique_numbers


random_numbers = generate_unique_numbers()
print("무작위로 생성된 중복되지 않는 숫자 10개:", random_numbers)
