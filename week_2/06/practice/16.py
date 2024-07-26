# 문제16) 재귀함수를 사용하여 주어진 문자열을 뒤집은 결과를 반환하는 함수를 구현하세요

def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]


print(reverse_string("hello"))
