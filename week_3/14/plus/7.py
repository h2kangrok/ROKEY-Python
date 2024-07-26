# MARK: 문제 7
# 7.	아래의 리스트에서 리스트 컴프리헨션을 활용해 행과 열이 바뀐 형태의 리스트를 새로 만들고, 이 변환된 리스트를 다음과 같이 출력하는 프로그램을 작성하시오.
# - 다음 리스트 컴프리헨션을 활용하세요.
# transpose = [[row[i] for row in m] for I in range(len(m[0]))]


m = [[1, 2], [3, 4], [5, 6], [7, 8]]

transpose = [[row[i] for row in m] for i in range(len(m[0]))]

print(transpose)
