# 6. 대소문자에 관계 없이, 문자열이 동일한 지 검사하는 파이썬 코드를 작성하시오(“조건” 파트를 완성).

my_input = 'abcd'
answer = "ABCD"

if my_input.lower() == answer.lower():
    print("Strings are equal")
else:
    print("Strings are not equal")
