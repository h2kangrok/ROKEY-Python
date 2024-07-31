# MARK: 문제 11

# 11.	제네레이터를 사용하여 데이터를 필터링하여 출력하는 프로그램을 작성하라.
# - ‘filter_even’ 제네레이터는 리스트 nums에서 짝수만 필터링하여 yield를 통해 반환합니다

def filter_even(nums):
    for num in nums:
        if num % 2 == 0:
            yield num


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


even_numbers = filter_even(nums)

for number in even_numbers:
    print(number)
