# 문제14) 입력받은 문자열이 팰린드롬(Palindrome: 앞으로 읽으나 뒤로 읽으나 동일한 문자열)인지 확인하는 프로그램을 작성하시오.

s = input("문자열을 입력해주세요. : ")

if s == "".join(reversed(s)):
    print("True")
else:
    print("False")
