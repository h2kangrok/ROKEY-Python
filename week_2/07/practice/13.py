
# 문제13) 〖a^3〗이 100을 넘는 최초 값을 반환하는 함수를 구현하고, 이를 사용하는 프로그 램을 작성한다.

def solution():
    a = 1
    while True:
        if a**3 > 100:
            return a
        a += 1


print(solution())
