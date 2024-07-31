# MARK: 문제 5

# 5.	사용자 정의 클래스를 이용하여 이터레이터를 구현하고, 주어진 리스트의 값을 반복적으로 출력하는 프로그램을 작성하라.
# numbers = [1, 2, 3, 4, 5]
# - MyIterator 클래스는 이터레이터 프로토콜에 따라 __iter__()와 __next__() 메서드를 구현합니다.
# - __init__() 메서드에서는 초기화를 수행하고, 입력으로 받은 데이터(data)와 현재 인덱스(index)를 초기화합니다.
# - __iter__() 메서드는 이터레이터 객체 자체를 반환합니다. 이는 이터레이터 프로토콜을 따르기 위해 필요한 메서드입니다.
# - __next__() 메서드는 다음 값을 반환합니다. 현재 인덱스(index)를 사용하여 데이터에서 값을 가져온 후, 인덱스를 증가시킵니다.
# 데이터를 모두 순회한 경우 StopIteration 예외를 발생시켜 반복을 멈춥니다.
# - MyIterator 객체를 생성하고, for 반복문을 사용하여 이터레이터를 순회하면서 각 값을 출력합니다.

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


numbers = [1, 2, 3, 4, 5]

my_iterator = MyIterator(numbers)

for number in my_iterator:
    print(number)
