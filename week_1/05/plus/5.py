# 5. 사용자로부터 입력받은 문자열이 비밀번호로 쓰기에 적합한지 판단하는 파이썬 코드를 작성하시오. 적합한 비밀번호는 아래 조건을 만족하는 비밀번호이다.
# 1.	문자열의 길이는 8이상 30이하여야 한다.
# 2.	문자열은 영문과 숫자로만 구성되어야한다.
# 3.	영문과 숫자를 모두 포함해야 한다.
# 4.	대소문자를 모두 포함해야 한다.

my_password = "abcdddddddddd12!@"


def is_valid_password(password):
    if not (8 <= len(password) <= 30):
        return False
    if not password.isalnum():
        return False

    contains_digit = any(char.isdigit() for char in password)
    contains_alpha = any(char.isalpha() for char in password)
    if not (contains_digit and contains_alpha):
        return False

    contains_upper = any(char.isupper() for char in password)
    contains_lower = any(char.islower() for char in password)
    if not (contains_upper and contains_lower):
        return False

    return True


if is_valid_password(my_password):
    print("비밀번호로 적합합니다.")
else:
    print("비밀번호로 적합하지 않습니다.")


my_password = "abcdddddddddd12가!@"


def is_valid_password(password):
    if not (8 <= len(password) <= 30):
        return False
    if not password.isalnum():
        return False

    contains_digit = any(char.isdigit() for char in password)
    contains_alpha = any(char.isalpha() for char in password)
    if not (contains_digit and contains_alpha):
        return False

    contains_upper = any(char.isupper() for char in password)
    contains_lower = any(char.islower() for char in password)
    if not (contains_upper and contains_lower):
        return False

    return True


if is_valid_password(my_password):
    print("비밀번호로 적합합니다.")
else:
    print("비밀번호로 적합하지 않습니다.")
