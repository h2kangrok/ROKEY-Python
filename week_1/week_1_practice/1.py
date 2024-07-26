# 1-1)
# 0 ~ 9 까지의 숫자중 한개를 입력하면, 가로 10, 세로 10인, 해당 캐릭터로 채워진 정방행렬 값을 출력 해본다

num = input("0 ~ 9까지의 숫자중 한개를 입력하세요. : ")

for _ in range(10):
    for _ in range(10):
        print(num, end="")
    print()
