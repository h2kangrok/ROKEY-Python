# 문제10) 문자열 “123456789”를 변수에 저장하고 첫 번째 줄에는 홀수만 두 번째 줄에는 짝수만 출력하는 프로그램을 작성하시오.

odd_list = []
even_list = []

s = "123456789"

for i in list(s):
    if int(i) % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print(*odd_list)
print(*even_list)
