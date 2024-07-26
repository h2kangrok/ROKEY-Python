# MARK: 문제 13
# 문제13) 정수 n1과 n2가 인자로 전달되면 n1, n1 + 1, n1 + 2, ..., n2 까지 각 정수의 약수들을 화면에 출력하는 함수를 구현한다.
# 이 함수를 이용해서 10~16까지의 약수 들을 출력해본다.

def solution(n1, n2):
    for i in range(n1, n2 + 1):
        divisors = []
        for j in range(1, i + 1):
            if i % j == 0:
                divisors.append(j)
        divisors_str = ', '.join(map(str, divisors))
        print(f"{i}의 약수는 {divisors_str}입니다.")


solution(10, 16)
