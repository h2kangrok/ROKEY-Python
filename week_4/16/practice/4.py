# MARK: 문제 4

# 4.	map 함수는 파이썬의 내장 함수로,
# 하나 이상의 시퀀스(ex: 리스트, 튜플 등)의 각 요소에 대해 지정된 함수를 적용하고,
# 그 결과를 담은 맵 객체(map object)를 반환합니다. (ex: map(function, iterable,,,)
# 문제3에서 만들어진 람다 함수와 제공된 리스트를 map 함수의 인자로 적용하는 코드를 작성해 보시오.

# 람다 함수 정의
# Write your code here

# 주어진 리스트
numbers = [1, 2, 3, 4, 5]

# map 함수를 사용하여 람다 함수를 numbers 리스트에 적용
result = map(lambda x: x**2 if x % 2 == 0 else x, numbers)

# map 객체를 리스트로 변환하여 출력
print(list(result))  # 출력: [1, 4, 3, 16, 5]
