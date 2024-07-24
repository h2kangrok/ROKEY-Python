# MARK: 문제 8

# 8.	두 개의 문자열이 주어졌을 때, 두 문자열에 공통으로 나타나는 문자를 모두 찾아서 집합으로 반환하는 함수를 작성하라.
# 여기서 공통 문자는 대소문자를 구분하지 않는다.
# <힌트>
# - 딕셔너리의 키와 값을 동시에 비교해야 합니다.
# - 딕셔너리 내포를 사용할 수 있습니다.
# - 조건문을 사용하여 키와 값을 동시에 체크합니다.

str1 = "Hello World"
str2 = "Python Programming"


def intersect(str1, str2):

    str1 = str1.lower()
    str2 = str2.lower()

    set1 = {char for char in str1 if char.isalpha()}
    set2 = {char for char in str2 if char.isalpha()}

    common_chars = set1 & set2

    return common_chars


print(intersect(str1, str2))
