# MARK: 문제 11
# 문제11) 정수 n을 인자로 전달 받고, n의 모든 약수를 리스트로 만들어 반환하는 함수를 구현한다. 이 함수를 이용해서 2~20까지의 정수에 대해 약수의 개수를
# 다음 형태로 출력하는 코드를 작성한다.

# 2의 약수개수: 2
# 3의 약수 개수: 2
# ...
# 19의 약수 개수: 2
# 20의 약수 개수: 6

def solution(n):
    divisors_list = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors_list.append(i)
    print(f"{n}의 약수 개수: {len(divisors_list)}")


for n in range(2, 21):
    solution(n)
