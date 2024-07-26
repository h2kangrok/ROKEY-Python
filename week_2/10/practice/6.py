# MARK: 문제 6

#  문제6) 함수 divide(x, y)  함수를 구현 한 후 연산 0으로 나누는 것에 대한 예외 처리를 수행하도록 한다.
# - 구문은 try, except, else 블록 구현
# - 다음 두 호출에 대한 결과
#      결과: 1.6
#      0으로는 나눌 수 없습니다.

def divide(x, y):
    try:
        answer = x / y
    except ZeroDivisionError:
        print("0으로는 나눌 수 없습니다.")
    else:
        return print(f"결과: {answer}")


try:
    divide(8, 5)
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")

try:
    divide(4, 0)
except ZeroDivisionError:
    print("0으로는 나눌 수 없습니다.")
