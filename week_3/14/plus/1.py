# #MARK: 문제 1
# 1.	아래 프로그램을 리스트 컴프리헨션을 사용한 코드로 변환하시오.
# even = []

# for i in range(2, 11, 2):
#       even.append(i)
# print(even)

even = [i for i in range(2, 11, 2)]
print(even)
