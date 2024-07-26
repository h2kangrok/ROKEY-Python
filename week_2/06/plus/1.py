# 1.  아래는 1부터 100까지 전부 더하는 방법을 두가지로 나누어 파이썬 코드로 작성한 것이다.
# 두 방법 중 더 효율적인 방법을 선택하고 그 이유를 서술하라.

# 1부터 100까지 재귀적으로 더함
def sum1(n):
    if n == 1:
        return 1
    return n + sum(n-1)

# 1부터 100까지 공식으로 더함


def sum2(n):
    return n * (n+1) // 2


print(sum(100))
print(sum2(100))
