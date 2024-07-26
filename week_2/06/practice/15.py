# 문제15) 최대공약수(Great Common Denominator) 구하기
# <알고리즘>
# - m = n이면 m 또는 n 반환
# - m > n이면 m –n과 n의 최대공약수 반환
# - m < n이면 m과 n –m의 최대공약수 반환
def gcd(m, n):
    if m == n:
        return m
    elif m > n:
        return gcd(m - n, n)
    else:
        return gcd(m, n - m)


print(gcd(48, 18))
