# MARK: 문제 3

# 문제3) 사용자로부터 입력을 받는 경우에는 오류가 발생하기 쉽다.
# s = input("정수를 입력하세요: ")
# n = int(s)

# try except 구문으로 예외처리 코드를 작성해 본다.
# 예외가 발생할 경우에는 "숫자를 입력하지 않았어요"라고 출력한다

try:
    s = input("정수를 입력하세요: ")
    n = int(s)
    print(f"입력한 정수는 {n}입니다.")
except ValueError:
    print("숫자를 입력하지 않았어요")
