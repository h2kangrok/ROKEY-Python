# 6. 주어진 정수 내에서 특정 숫자가 몇 번 등장하는지 세는 재귀 함수를 작성하라(필요시 함수의 인자를 수정할 수 있다).

def count_number(n, x):
    if n == 0:
        return 0
    if n % 10 == x:
        return 1 + count_number(n // 10, x)
    else:
        return count_number(n // 10, x)


print(count_number(123412341, 1))
