# MARK: 문제 9

# 9.	문제8에서 작성된 프로그램을 람다 함수를 이용하는 프로그램으로 변화해서 실행해 보시오.

words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

print(list(filter(lambda word: 'a' in word, words)))
