# MARK: 문제 4
# 4.	다음과 같은 내용을 가진 리스트와 튜플이 있다. 튜플을 리스트에 연결하는 코드를 작성하시오.
list_1 = [1, 2, 3]
tup_1 = (4, 5, 6)

combined_list = list_1 + list(tup_1)
print("방법 1:", combined_list)

list_1.extend(tup_1)
print("방법 2:", list_1)
