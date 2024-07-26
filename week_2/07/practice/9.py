# 문제9) 정수 n1과 n2가 인자로 전달되면 n1, n1 + 1, n1 + 2, ..., n2 까지 각 정수의 약수들을 화면에 출력하는 함수를 구현한다.
# 이 함수를 이용해서 10~16까지의 약수 들을 출력해본다.

def divisor_of_an_integer(n1, n2):
    for i in range(n1, n2 + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                print(j, end=" ")
        print()


divisor_of_an_integer(10, 16)
