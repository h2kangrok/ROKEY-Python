# MARK: 문제 6
# 6.	아래 두 리스트의 각 요소를 조건에 따라 계산하는 일반 함수를 작성하시오
# - 조건: list1의 요소가 짝수이면 list2의 요소를 더하고, 그렇지 않으면 곱함
# - 결과를 출력하시오.
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]


# def solution(list1, list2):
#     for i in range(0, len(list1)):
#         if list1[i] % 2 == 0:
#             list1[i] += list2[i]
#         else:
#             list1[i] *= list2[i]
#     return list1


# print(solution(list1, list2))

def solution(list1, list2):
    result = []
    for x, y in zip(list1, list2):
        if x % 2 == 0:
            result.append(x + y)
        else:
            result.append(x * y)
    return result


print(solution(list1, list2))
