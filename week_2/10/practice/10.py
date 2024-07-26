# MARK: 문제 10


# 문제10) 사용자로부터 두 개의 숫자와 연산자를 입력받아 사칙연산(+, -, *, /)을 수행 하는 프로그램을 작성하세요.
# 잘못된 입력이나 연산에서 발생할 수 있는 예외를 처리하고, 계산이 성공했는지 여부에 따라 메시지를 출력하세요.

def calculator():
    try:
        num1 = float(input("첫 번째 숫자를 입력하세요: "))
        num2 = float(input("두 번째 숫자를 입력하세요: "))
    except ValueError:
        print("잘못된 입력입니다. 숫자를 입력해주세요.")
    else:
        operator = input("연산자를 입력하세요 (+, -, *, /): ")

        if operator == "+":
            result = num1 + num2
            print(f"합 계산에 성공했습니다. 결과: {result}")
        elif operator == "-":
            result = num1 - num2
            print(f"빼기 계산에 성공했습니다. 결과: {result}")
        elif operator == "*":
            result = num1 * num2
            print(f"곱 계산에 성공했습니다. 결과: {result}")
        elif operator == "/":
            try:
                result = num1 / num2
                print(f"나누기 계산에 성공했습니다. 결과: {result}")
            except ZeroDivisionError:
                print("0으로 나누기 계산이 불가능 합니다.")
        else:
            print("존재하지 않는 연산자입니다.")
    finally:
        print("프로그램을 종료합니다.")


calculator()
