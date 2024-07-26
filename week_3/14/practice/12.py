# MARK: 문제 12

# 12.	리스트 strings에서 중복되는 단어를 제거하고 리스트의 메소드인 sort() 함수을 사용하여
# 오름차순으로 정렬된 리스트를 출력하는 코드를 작성하시오.

strings = ["mango", "apple", "banana",
           "cherry", "date", "fig", "apple", "banana"]
strings_2 = list(set(strings))
strings_2.sort()
print(strings_2)
