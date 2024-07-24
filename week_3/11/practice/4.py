# MARK: 문제 4
# 4.	두 개의 딕셔너리가 주어졌을 때, 두 딕셔너리에서 키와 값이 모두 같은 (공통된) 항목을 찾아서 새로운 딕셔너리로 반환하는 함수를 작성하세요.
# dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# dict2 = {'a': 1, 'b': 2, 'c': 4, 'e': 5}
# 공통된 키-값 쌍:{'a': 1, 'b': 2}

# dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# dict2 = {'a': 1, 'b': 2, 'c': 4, 'e': 5}

# dict3 = {}

# for key1, value1 in dict1.items():
#     for key2, valeu2 in dict2.items():
#         if key1 == key2 and value1 == valeu2:
#             dict3[key1] = value1

# print(f"공통된 키-값 쌍: {dict3}")

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict2 = {'a': 1, 'b': 2, 'c': 4, 'e': 5}


def find_common_items(dict1, dict2):
    common_dict = {}

    for key in dict1:
        if key in dict2 and dict1[key] == dict2[key]:
            common_dict[key] = dict1[key]

    return common_dict


print("공통된 키-값 쌍:", find_common_items(dict1, dict2))
