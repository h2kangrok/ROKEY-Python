# 4. 주어진 정수의 각 자릿수의 합을 더하는 재귀 함수를 작성하라(필요시 함수의 인자를 수정할 수 있다).

# 예제
# Input: 4321
# Output: 10

# Input: 573563
# Output: 29

# 예제코드

def sum_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_digits(n // 10)


print(f"Input: 4321")
print(f"Output: {sum_digits(4321)}")
