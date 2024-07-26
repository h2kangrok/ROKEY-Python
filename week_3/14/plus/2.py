# MARK: 문제 2

# 2.	아래와 같이 if 조건문이 있는 반복문으로 리스트를 생성하는 프로그램을 리스트 컴프리헨션을 적용한 프로그램으로 작성하시오.

# s = []
# for i in range(10):
#     if i % 2 == 1:
#         s.append(i**2)
# print(s)


# Write your code here: 위 코드를 List comprehension으로 변환하시오.

# s = [i**2 for i in range(10) if i % 2 == 1]
# print(s)

mylist = [1, 5, 1, 7, 1]
mylist[mylist.count(1)] = 70
mylist[len(mylist) - 1] = 80
mylist.insert(1, 50)
print(mylist)
