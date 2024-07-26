# MARK: 문제 6

# 6.	다음 중첩된 리스트 data에서 각 행의 합과 열의 합을 리스트 rsum과 csum에 저장해 출력하는 프로그램을 작성하시오.

data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]


def sums(data):
    # 행의 합
    rsum = [sum(row) for row in data]

    # 열의 합
    csum = [sum(data[i][j] for i in range(len(data)))
            for j in range(len(data[0]))]

    return rsum, csum


rsum, csum = sums(data)

print("행의 합:", rsum)
print("열의 합:", csum)
