# 4. 파이썬에서는 변수명을 만들기 위한 다양한 조건이 존재한다. 사용자로부터 입력받은 문자가 변수명으로 적합한지 판단하는 파이썬 코드를 작성하시오.
# ●	단 편의를 위해 아래 조건만 만족하면 올바른 변수명이라고 판단한다.
# ○	첫글자는 영문 혹은 “_”로 시작해야 한다.
# ○	나머지는 영문 혹은 숫자로 구성되어야 한다.

# 아래의 예제코드를 적절히 완성하라


my_var1 = "num1_"


def is_valid_variable_name(name):
    if not name:
        return False
    if not (name[0].isalpha() or name[0] == "_"):
        return False
    for char in name[1:]:
        if not (char.isalnum() and char.isascii()):
            return False
    return True


if is_valid_variable_name(my_var1):
    print("Variable name is valid")
else:
    print("Variable name is invalid")
