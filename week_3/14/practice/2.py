# MARK: 문제 2

# 2.	정수 1부터 100 까지의 요소를 가진 시퀀스 자료형을 만들고,
# 정수 숫자를 입력 받아 자료안에 있는지 확인해서 True/False로 알려주는 간단한 프로그램을 작성하시오.


def solution():

    num_list = list(range(1, 101))

    try:
        num = int(input("정수 숫자를 입력하세요 : "))
        if num in num_list:
            return True
        else:
            return False

    except ValueError:
        print("정수를 입력하세요.")
        return False


print(solution())
