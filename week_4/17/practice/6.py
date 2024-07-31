# MARK: 문제 6

# 6.	문제5번에서 만들어진 이터레이터는 리스트의 요소들에 대해 순차적인 접근만 허용한다.
# 인덱스로 접근할 수 있는 방법을 찾아 프로그램을 수정하라.

# - 클래스에서 __getitem__ 메소드를 구현하면 인덱스로 접근 가능.

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

    def __getitem__(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            raise IndexError("인덱스가 범위를 벗어났습니다.")


numbers = [1, 2, 3, 4, 5]

iterator = MyIterator(numbers)

for num in iterator:
    print(num)

print("Index access:")
print(iterator[0])
print(iterator[3])
