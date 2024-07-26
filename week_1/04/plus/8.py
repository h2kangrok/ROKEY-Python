# MARK: 문제 8
# 문제 8번

num = list(map(int, input("4개의 정수를 입력하세요. : ").split()))
num.sort(reverse=True)

for i in num:
    print(i, end=" ")
