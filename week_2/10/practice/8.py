# MARK: 문제 8

# 문제8) 사용자로부터 입력받은 문자열을 정수로 변환할 때 발생할 수 있는 예외를 처리하세요.
# - try, except(value error), else, finally 블록을 사용할 것


def solution():
    try:
        s = input("정수로 변환할 문자열을 입력하세요. : ")
        change_int = int(s)
    except ValueError:
        print("정수로 변환할 수 없습니다.")
    else:
        print(F"{change_int} -> 정수로 변환이 되었습니다.")
    finally:
        print("예외처리가 잘 되었습니다.")


solution()
