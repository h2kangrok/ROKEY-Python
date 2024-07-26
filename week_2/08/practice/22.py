# MARK: 문제 22

# 문제22) 1에서 99까지의 난수 10개로 리스트를 만든 후, 다시 이 리스트를 튜플로 변환 하고,
# 다시 정렬된 리스트로 만들어서 전체의 합, 최대값, 최소값, 평균을 구하는 코드를 작성하시오.

import random

random_list = []
for i in range(10):
    random_list.append(random.randint(1, 99))
print(f"튜플로 변환: {tuple(random_list)}")
# 다시 정렬된 리스트
random_list.sort()
print(f"정렬된 리스트: {random_list}")
print(f"전체의 합: {sum(random_list)}")
print(f"최대값 : {max(random_list)}")
print(f"최소값 : {min(random_list)}")
print(f"평균값 : {sum(random_list) / len(random_list)}")
