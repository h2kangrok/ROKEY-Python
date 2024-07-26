# 문제5) 1부터 100까지의 합계를 계산하는 재귀함수를 작성한다.

def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)


print(sum(100))
