# MARK: 문제 16
# 문제16) 정수 한 개(n)를 함수의 인자로 받고, 그 정수의 모든 약수를 리스트로 구성해서 반환하는 함수(createDivisorsList)를 구현.
# 이 함수를 이용해서 사용자로부터 1~1000 정수 중에서 하나를 입력 받고, 그것의 모든 약수들의 합을 계산해서 출력 하는 프로그램 작성
# - 정수 n의 약수를 찾는 방법은 1~n까지의 정수를 n으로 나눠서 나머지가 0인지 확인
# <요구사항>
# - 입력 받는 값은 1~1000 정수로 가정
# - createDivisorsList함수를 호출하는 코드에서 리스트의 내용을 화면에 출력함.

def createDivisorsList(n):

    divisors_list = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors_list.append(i)
    return divisors_list


def main():
    while True:
        try:
            n = int(input("1 ~ 1000 사이의 정수 한 개를 입력하세요: "))
            if 1 <= n <= 1000:
                divisors_list = createDivisorsList(n)
                print(f"{n}의 약수들: {divisors_list}")

                divisors_sum = sum(divisors_list)
                print(f"{n}의 약수들의 합: {divisors_sum}")

                break
            else:
                print("1 ~ 1000 사이의 정수를 입력하세요.")
        except ValueError:
            print("유효한 숫자를 입력하세요.")


main()
