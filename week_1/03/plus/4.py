# MARK: 문제 4
# 문제4) 아래와 같이 다이아몬드 패턴을 출력하는 코드를 작성하시오.

for i in range(1, 14, 4):
    for j in range(1, i+1):
        print("*", end=" ")
    print()
    if i == 13:
        for k in range(9, 0, -4):
            for l in range(1, k+1):
                print("*", end=" ")
            print()

for i in range(1, 14, 4):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
for k in range(9, 0, -4):
    for l in range(1, k + 1):
        print("*", end=" ")
    print()
