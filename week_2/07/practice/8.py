# 문제8) 정수의 약수를 화면에 출력하는 프로그램 작성.
# - 정수를 한 개 인자로 전달받고, 약수를 화면에 모두 출력하는 함수 작성.
# - 테스트로 12와 16을 실행해 볼 것.

def divisor_of_an_integer(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")
    print()


divisor_of_an_integer(12)
divisor_of_an_integer(16)
