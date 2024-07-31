# MARK: 문제 11
# 1.	패스워드 규칙을 검사하는 정규표현식을 사용한 코드를 작성해 보시오.
# - 패스워드 규칙은 보안을 강화하기 위해 다양한 조건을 만족해야 할 수 있습니다.
# 최소길이, 대소문자 포함 여부, 숫자 포함 여부, 특수문자 포함 여부 등이 있습니다.
# - 패스워드 규칙을 검사하는 함수(함수명: check_password_strength)를 만들고,
# 패스워드를 입력하면 패스워드의 통과여부를 알려준다.

import re


def check_password_strength(password):
    # 최소 8자 이상, 숫자와 특수문자를 포함하는지 확인하는 정규표현식
    pattern = r'^(?=.*[0-9])(?=.*[!@#$%^&*])(?=.*[a-zA-Z]).{8,}$'

    if re.match(pattern, password):
        return True
    else:
        return False


# 테스트
password1 = "StrongPassword123!"
print(
    f"Password '{password1}' is strong: {check_password_strength(password1)}")

newPswd = input('\n패스워드를 입력하세요: ')
if check_password_strength(newPswd):
    print('안전한 패스워드입니다.')
else:
    print('패스워드의 기준에 맞지 않습니다')
