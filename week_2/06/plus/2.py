# 2. 재귀함수를 이용하여 문자열을 뒤집는 함수를 작성하라(필요시 함수의 인자를 수정할 수 있다).
# 예제
# Input: “ABCD”
# Output” “DCBA”

def reverse_string(s):
    if len(s) <= 1:
        return s
    else:
        return reverse_string(s[1:]) + s[0]


print(f"Input: \"ABCD\"")
print(f"Output: \"{reverse_string('ABCD')}\"")
