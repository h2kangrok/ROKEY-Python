# MARK: 문제 9
# \9.	영문 알파벳, 특수문자, 숫자로만 구성된 비밀 번호 문자열을 입력 받고, 아래 표를 기준으로 어느 정도안전한가를 출력하는 프로그램을 작성한다.
# 표) 비밀번호 안전도 점검 기준(기본적으로 조건은 and임)

# 특수 문자는 키보드로 입력할 수 있는 문자들을 나타내는 것으로,"~`!\@#$%^&:',./?><|“로 가정한다.

import re


def password_strength(password):
    # 패스워드 길이 검사
    length = len(password)

    # 특수 문자, 숫자, 대문자 검사
    special_char_count = len(re.findall(r"~`!\@#$%^&:',./?><|", password))
    digit_count = len(re.findall(r'\d', password))
    uppercase_count = len(re.findall(r'[A-Z]', password))

    # 조건에 따른 비밀 번호 강도 판단
    if length > 10 and special_char_count >= 2 and digit_count >= 1 and uppercase_count >= 1:
        return "안전함"
    elif 8 <= length <= 10 and special_char_count >= 1 and digit_count >= 1:
        return "보통"
    elif 8 <= length <= 10 and (special_char_count >= 1 or digit_count >= 1 or uppercase_count >= 1):
        return "보통 이하"
    else:
        return "안전하지 않음"


def main():
    try:
        password = input("비밀 번호를 입력하세요: ")

        if re.match(r'^[a-zA-Z0-9!@#$%^&*(),.?":{}|<>]+$', password):
            strength = password_strength(password)
            print(f"비밀 번호 강도: {strength}")
        else:
            print("비밀 번호는 영문 알파벳, 특수문자, 숫자로만 구성되어야 합니다.")

    except Exception as e:
        print(f"오류가 발생했습니다: {e}")


if __name__ == "__main__":
    main()
