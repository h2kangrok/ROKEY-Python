# MARK: 문제 2
# 2.	리스트 numbers를 이터레이터로 만들고 이터레이터 함수 next를 통해 리스트 요소의 값을 출력하는 프로그램을 작성하시오.

numbers = [1, 2, 3, 4, 5]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

try:
    print(next(iterator))
except StopIteration:
    print("리스트의 모든 요소를 다 순회했습니다.")
