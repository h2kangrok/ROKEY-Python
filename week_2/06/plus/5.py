# 5. 주어진 문자열이 회문인지 판단하는 재귀 함수를 작성하라(필요시 함수의 인자를 수정할 수 있다).
# ●	회문: 앞으로 읽으나 뒤로 읽으나 같은 순서로 나열되는 문자열

def isPalindrome(s):
    s = s.strip()

    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return isPalindrome(s[1:-1])


print(isPalindrome("hello"))
print(isPalindrome("level"))
