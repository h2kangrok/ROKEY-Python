# 문제17) 동전을 던져서 앞/뒷면이 나오는 횟수를 세고, ½ 확률에 수렴하는지 확인하는 프로그램을 작성한다. 컴퓨터에서 동전을 던질 수는 없으므로,
# random.randint()
# 함수를 이용해서 두 개 숫자 중 한 개를 무작위로 생성하여 동전의 앞/뒷면을 대신 한다.
# 100, 1000, 10000회 던져서 앞/뒷면이 나오는 횟수를 각각 출력한다.
# <요구사항>
# - 정해진 횟수만큼 동전을 던지고 앞/뒷면이 나오는 횟수를 출력하는 함수를 구현
# - 동전을 던지는 횟수는 함수에 입력으로 전달
# - 앞/뒷면이 나오는 확률을 구해서 각각 출력

import random


def flipCoin(num_throws):
    countFront = 0
    countBack = 0

    # 동전 던지기 시뮬레이션
    for _ in range(num_throws):
        if random.randint(0, 1) == 0:
            countFront += 1
        else:
            countBack += 1

    front_probability = countFront / num_throws
    back_probability = countBack / num_throws

    print(f"{num_throws}번 던짐")
    print(f"앞면 횟수: {countFront}, 확률: {front_probability:.4f}")
    print(f"뒷면 횟수: {countBack}, 확률: {back_probability:.4f}")
    print()


for throws in [100, 1000, 10000]:
    flipCoin(throws)
