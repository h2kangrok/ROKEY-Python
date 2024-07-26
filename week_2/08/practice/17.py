# MARK: 문제 17
# 문제17) 정수 한 개(n)를 함수의 인자로 받고, 그 정수의 n개만큼 사용자로부터 정수를 입력 받아서, 이를 요소로 튜플을 구성한 후 함수의 결과값으로 반환하는 함수를 작성.
# 이 함수를 이용해서 n개의 정수 값으로 구성된 튜플을 생성하고 출력하는 프로그램 작성
# <요구사항>
# - 사용자가 입력한 정수의 개수는 함수에 인자로 전달
# - 사용자로부터 입력 받는 값은 양의 정수만으로 가정
def change_tuple(n):
    n_list = []
    for _ in range(n):
        while True:
            try:
                num = int(input("튜플에 들어갈 정수를 입력하세요: "))
                if num <= 0:
                    print("양의 정수를 입력해야 합니다. 다시 입력하세요.")
                else:
                    n_list.append(num)
                    break
            except ValueError:
                print("유효한 정수를 입력하세요.")
    return tuple(n_list)


def main():
    while True:
        try:
            n = int(input("정수 한 개를 입력하세요: "))
            if n <= 0:
                print("양의 정수여야 합니다.")
            else:
                print("생성된 튜플:",  change_tuple(n))
                break
        except ValueError:
            print("유효한 숫자를 입력하세요!")


main()
