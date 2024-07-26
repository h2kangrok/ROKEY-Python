# MARK: 문제 10
# 10.	슬라이스를 이용하여 입력되는 단어가 팰린드롬(Palindrome) 인지 확인하는 프로그램을 작성하시오.
# 팰린드롬: 앞에서부터 읽으나 뒤에서부터 읽으나 동일한 문자열을 의미

def solution():
    str_input = input("단어를 입력해주세요 : ").lower()
    return str_input == str_input[::-1]


if solution():
    print("팰린드롬입니다.")
else:
    print("팰린드롬이 아닙니다.")
