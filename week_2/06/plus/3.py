# 3. 주어진 정수가 소수인지 아닌지 판단하는 재귀 함수를 작성하라(필요시 함수의 인자를 수정할 수 있다).

# 예제
# Input: 7
# Output: True

# Input: 12
# Output: False

def is_prime(n, i=2):
    if n <= 1:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False

    return is_prime(n, i + 1)


print(f"Input: 7")
print(f"Output: {is_prime(7)}")
