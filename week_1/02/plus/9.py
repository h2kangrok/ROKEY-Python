# MARK: 문제 9
# 문제9) 사용자로부터 입력받은 문자열에서 모든 숫자를 추출하여 그 합을 계산하는 프로그램을 작성하시오.
# - 문제5의 isdigit() 이용
# - for 반복문을 이용

input = input("문자열을 입력하세요. : ")
sum = 0
for i in input:
    if i.isdigit():
        sum += int(i)
print(sum)
