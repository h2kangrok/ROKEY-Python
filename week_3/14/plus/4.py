# MARK: 문제 4
# 4.	1에서 99까지의 난수 10개로 리스트를 만든 후
# 리스트와 정렬된 리스트 그리고 내림차순으로 정렬된 역순 리스트를 출력하는 프로그램을 작성하시오.
import random

random_list = list(random.sample(range(1, 100), 10))

print(random_list.sort())
random_list.sort(reverse=True)
print(random_list)
