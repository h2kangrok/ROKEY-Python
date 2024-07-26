# 1-2)
# 0 ~ 9 까지의 숫자중 한개를 입력하면, 사용자가 입력한 숫자 캐릭터로 가로 10, 세로 10인 정방행렬을 채우고, 정삼각형을 출력하는 파이썬 코드를 만들자
num = input("0 ~ 9까지의 숫자중 한개를 입력하세요. : ")

for i in range(1, 7):
    for k in range(7-i):
        print(' ', end='')
    for k in range(i*2-1):
        print(num, end='')
    print()
