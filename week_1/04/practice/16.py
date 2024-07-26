# MARK: 문제 16

# 문제 16번

import random

random_numbers = [random.randint(1, 99) for _ in range(3)]
max_number = max(random_numbers)

print("가장 큰 정수 : ", max_number)
