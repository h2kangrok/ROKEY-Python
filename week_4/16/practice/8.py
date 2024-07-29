# MARK: 문제 8

# 8.	아래 리스트에 있는 문자열 중 ‘a'를 포함하는 단어를 걸러내는 프로그램을 filter 함수를 사용하여 작성하시오
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]


def contains_a(word):
    return "a" in word

print(list(filter(contains_a, words)))
