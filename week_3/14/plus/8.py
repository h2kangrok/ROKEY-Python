# MARK: 문제 8
# 8.	1에서 20까지의 난수 5개를 두 번 얻어 각각 집합인 변수 A, B에 저장한다.
# 집합 A와 B의 합집합과 교집합, 차집합, 여집합을 구해 출력하는 프로그램을 작성하시오.

# 모듈 random의 sample() 함수를 사용한 다음 문장을 집합 변수 A에 저장

from random import sample

# 1에서 20까지의 난수 5개를 두 번 얻어 각각 집합 A, B에 저장
A = set(sample(range(1, 21), 5))
B = set(sample(range(1, 21), 5))

# 집합 연산 수행
union = A | B  # 합집합
intersection = A & B  # 교집합
difference_A_B = A - B  # A의 차집합 B
difference_B_A = B - A  # B의 차집합 A
complement_A = set(range(1, 21)) - A  # A의 여집합
complement_B = set(range(1, 21)) - B  # B의 여집합

# 결과 출력
print("집합 A:", A)
print("집합 B:", B)
print("합집합 (A ∪ B):", union)
print("교집합 (A ∩ B):", intersection)
print("A의 차집합 B (A - B):", difference_A_B)
print("B의 차집합 A (B - A):", difference_B_A)
print("A의 여집합:", complement_A)
print("B의 여집합:", complement_B)
