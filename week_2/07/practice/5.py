# 문제5) 사용자로부터 숫자 5개를 입력받고, 가장 큰 값을 찾아서 반환하는 함수를 작성하고, 가장 큰 입력값을 출력하는 프로그램을 작성하시오.
# <요구사항>
# - 입력되는 숫자 5개는 모두 0보다 큰 양수로 가정함.
# - 자료의 정렬 알고리즘이 적용된 함수를 사용하지 않음.

nums = input("사용자로부터 숫자 5개를 입력하세요.ex) 2 3 4 : ").split()


def maxNum(nums):
    max = 0
    for i in range(0, len(nums)-1):
        if nums[i] >= nums[i+1]:
            max = nums[i]
        else:
            max = nums[i+1]
    return max


print(f"가장 큰 입력값은: {maxNum(nums)}")

nums = list(map(int, input("사용자로부터 숫자 5개를 입력하세요 (공백으로 구분): ").split()))


def maxNum(nums):
    max_val = nums[0]
    for num in nums:
        if num > max_val:
            max_val = num
    return max_val


print(f"가장 큰 입력값은: {maxNum(nums)}")
