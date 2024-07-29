# MARK: 문제 7

# 7.	문제6의 함수를 람다 함수로 변환해서 프로그램을 실행해 보시오
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

print(list(map(lambda x, y: x + y if x % 2 == 0 else x * y, list1, list2)))
