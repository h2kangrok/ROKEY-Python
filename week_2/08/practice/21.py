# MARK: 문제 21

# 문제21) 아래의 중첩된 리스트를 for문으로 행과 열을 맞춰 출력한 후, 다시 행과 열을 바꾼 형태로 출력하세요.
# lst = [[1,2],[3,4],[5,6],[7,8]]
# 결과: 1 3 5 7
#          2 4 6 8

lst = [[1, 2], [3, 4], [5, 6], [7, 8]]

print("행과 열을 맞춰 출력:")
for row in lst:
    print(row[0], row[1])

print("\n행과 열을 바꾼 형태로 출력:")
for i in range(len(lst[0])):
    for j in range(len(lst)):
        print(lst[j][i], end=" ")
    print()
