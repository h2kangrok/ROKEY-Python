# 문제16) 두 개의 문자열을 입력받아 두 문자열이 아나그램(Anagram: 두 개의 단어나 구를 구성하는 문자들을 재배열하여 다른 문자열을 만드는 경우:
# 예를 들면 “listen"과 ”silent"는 아나그램입니다. 또 다른 예는 “debit card"와 ”bad credit"도 아나그램입니다.)인지
# 확인하는 프로그램을 작성해 보시오.
# - sorted 함수를 이용한다.

s1 = input("첫 번째 문자열을 입력해주세요. : ")
s2 = input("두 번째 문자열을 입력해주세요. : ")

sorted_s1 = sorted(s1)
sorted_s2 = sorted(s2)

if sorted_s1 == sorted_s2:
    print(f"\"{s1}\"와 \"{s2}\"는 아나그램입니다.")
else:
    print(f"\"{s1}\"와 \"{s2}\"는 아나그램이 아닙니다.")
