# MARK: 문제 15
# 문제15) 정수 한 개(n)를 함수의 인자로 받고, 그 정수의 n개만큼 사용자로부터 정수를 입력 받아서 이를 요소로 리스트를 구성한 후 함수의 결과값으로 반환하는
# 함수 작성.  이 함수를 이용해서 n개의 정수 값으로 구성된 리스트를 생성하고 출력하는 프로그램 작성.
# <요구사항>
# - 사용자로부터 입력받을 정수의 개수는 함수에 인자로 전달
# - 사용자로부터 입력받는 값은 양의 정수로 가정

def solution(n):
    n_list = []
    for i in range(n):
        while True:
            try:
                num = int(input("리스트에 들어갈 정수를 입력하세요: "))
                if num <= 0:
                    print("양의 정수를 입력해야 합니다. 다시 입력하세요.")
                else:
                    n_list.append(num)
                    break
            except ValueError:
                print("유효한 정수를 입력하세요.")
    print("입력된 리스트:", n_list)


try:
    n = int(input("정수 한 개를 입력하세요: "))
    if n <= 0:
        print("정수는 양의 정수여야 합니다.")
    else:
        solution(n)
except ValueError:
    print("유효한 정수를 입력하세요.")
