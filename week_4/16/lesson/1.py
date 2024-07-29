# def plus_ten(x): return x + 10


# print(plus_ten(10))

# def cube_volume_lambda(a): return a*a*a


# print(f'The volume of lambda function is {cube_volume_lambda(3.14)}.')

# def mult_table(n):
#     return lambda x: x*n


# n = int(input('Enter a number: '))
# y = mult_table(n)
# print(f'The entered number is {n}, which is a perfect number.')
# for i in range(11):
#     print(('%d x %d = %d' % (n, i, y(i))))

# from functools import reduce


# def f(x, y):
#     return x + y


# a = [1, 2, 3, 4, 5]
# print(reduce(f, a))

# from functools import reduce
# numbers = [3, 4, 6, 9, 34, 12]


# def custom_sum(first, second):
#     return first + second


# result = reduce(custom_sum, numbers, 10)
# print(result)

# from functools import reduce
# a = [1, 2, 3, 4, 5]
# print(reduce(lambda x, y: x + y, a))

# people = [
#     {"name": "John", "age": 45},
#     {"name": "Diana", "age": 32},
#     {"name": "Tom", "age": 20}
# ]

# sorted_people = sorted(people, key=lambda x: x["age"])

# print(sorted_people)

# from functools import reduce
# numbers = [5, 8, 6, 10, 9, 2]
# max_number = reduce(lambda x, y: x if x > y else y, numbers)
# # 결과 출력
# print(max_number)  # 리스트에서 가장 큰 숫자 출력

# words = ["hello", "world", "python", "programming"]
# capitalized_words = list(map(lambda word: word.capitalize(), words))
# # 결과 출력
# print(capitalized_words)  # 각 단어의 첫 글자를 대문자로 변환한 리스트 출력

products = [
    {"name": "Product A", "price": 150, "stock": 5},
    {"name": "Product B", "price": 120, "stock": 12},
    {"name": "Product C", "price": 50, "stock": 20},
    {"name": "Product D", "price": 200, "stock": 9}
]
filtered_products = list(filter(lambda p: p['price'] > 100 and p['stock'] >=
                                10, products))
# 결과 출력
print(filtered_products)  # 조건에 맞는 제품들만 포함하는 리스트 출력
