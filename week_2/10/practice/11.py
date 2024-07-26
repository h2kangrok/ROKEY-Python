# MARK: 문제 11

#  문제11) 사용자로부터 여러 개의 숫자를 입력받아 합계를 계산하는 프로그램을 작성하세요.
# 이 프로그램은 다음의 기능을 포함해야 합니다:
# - 사용자가 입력한 문자열은 쉼표로만 구분되어 있다.(ex: 1,2,3,4).
# - 사용자가 입력한 문자열을 쉼표(,)로 분리하여 각 숫자를 추출합니다.
# - 숫자가 아닌 값이 포함되어 있는 경우 예외를 처리합니다.
# - 사용자가 입력한 숫자의 합계를 계산하여 출력합니다.
# - 예외가 발생한 경우 오류 메시지를 출력하고, 합계 계산을 건너뜁니다.

def solution(s_input):
    try:
        if "," not in s_input:
            raise ValueError("입력 형식이 잘못되었습니다. 쉼표로 구분된 숫자를 입력해주세요.")

        parts = s_input.split(",")
        numbers = [float(part) for part in parts]

        add_numbers = sum(numbers)
        return add_numbers
    except ValueError:
        raise ValueError("입력 형식이 잘못되었습니다. 숫자만 포함되어야 합니다.")


try:
    s_input = input("쉼표로 구분된 문자열을 입력해주세요. (ex: 1,2,3,4) : ")
    result = solution(s_input)
    print(f"사용자가 입력한 숫자의 합계는 : {result}")
except ValueError as e:
    print(e)
