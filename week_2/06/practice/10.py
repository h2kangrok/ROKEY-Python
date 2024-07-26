# 문제10) 세 개 단어로 구성된 문자열을 첫번째 인자로, 1부터 3까지의 정수값을 두번째 인자로 전달 받는 함수를 구현한다.
# 함수는 두번째 인자 위치에 해당되는 단어를 문자열로 반환한다.

# >>> print(getWord("A beautiful day", 1))
# A
# >>> print(getWord("A beautiful day", 3))
# day


def getWord(s, num):
    return s.split()[num-1]


print(getWord("A beautiful day", 1))
print(getWord("A beautiful day", 3))
