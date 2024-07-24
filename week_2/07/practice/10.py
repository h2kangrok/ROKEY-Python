# 문제10) 주사위에서 나올 수 있는 범위인 1~6사이의 정수 5개를 무작위로 출력하는 코드를 작성하세요.
# 중복되는 숫자가 있는지 세어보세요.


import random
from collections import Counter

numbers = [random.randint(1, 6) for _ in range(5)]

print(f"정수 5개: {' '.join(map(str, numbers))}")

count = Counter(numbers)
found = False

for num in range(1, 7):
    if count[num] > 1:
        print(f"중복된 숫자 {num}: {count[num]}개")
        found = True

if not found:
    print("중복된 숫자가 없습니다.")
