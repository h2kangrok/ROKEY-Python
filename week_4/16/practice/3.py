# MARk: 문제 3
n = int(input("정수를 입력하세요 : "))


def solution(x):
    # 람다 함수 반환
    return lambda x: x**2 if x % 2 == 0 else x


result = solution(n)
print(f"입력값: {n}, 처리된 결과: {result(n)}")
