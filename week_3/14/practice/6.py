# MARK: 문제 6

# 6.아래의 튜플에서 한 요소를 삭제한 후 새로운 튜플을 만드는 코드를 작성하시오.
# 요소를 삭제할 때 리스트 컴프리헨션(List comprehension) 구문을 사용할 것.
my_tuple = (1, 2, 3, 4, 5)
my_tuple = (1, 2, 3, 4, 5)

element_to_remove = 3

new_tuple = tuple(x for x in my_tuple if x != element_to_remove)

print("원래 튜플:", my_tuple)
print("새로운 튜플:", new_tuple)

# alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# print(alp[1:5])
# print(alp[-1:-6])
# print(alp[:])
# print(alp[1::2])
# print(alp[-2:-10:-3])
# print(alp[3:-1:2])
