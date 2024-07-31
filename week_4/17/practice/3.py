numbers = [1, 2, 3, 4, 5]

iterator = iter(numbers)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        print("리스트의 모든 요소를 다 순회했습니다.")
        break
