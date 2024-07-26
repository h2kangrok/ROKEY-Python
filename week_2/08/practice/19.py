# MARK: 문제 19

# 문제19) 다음 중첩된 리스트 data에서 각 행의 합과 열의 합을 리스트 rsum과 sum에 저장해 출력하는 프로그램을 작성하시오.
data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]


def rsum(data):
    row_sums = []
    for i in range(len(data)):
        row_sums.append(sum(data[i]))
    return row_sums


def colsum(data):
    col_sums = []
    for j in range(len(data[0])):
        column_sum = 0
        for k in range(len(data)):
            column_sum += data[k][j]
        col_sums.append(column_sum)
    return col_sums


row_sums = rsum(data)
col_sums = colsum(data)

print("행의 합:", row_sums)
print("열의 합:", col_sums)
