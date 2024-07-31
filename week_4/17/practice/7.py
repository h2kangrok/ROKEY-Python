# MARK: 문제 7
# 7.	텍스트 파일의 각 줄을 반환하는 이터레이터 함수 file_line_iterator를 구현하라.
# - file_line_iterator 함수는 파일 경로를 입력으로 받고, 이터레이터를 반환합니다.
# - 반환된 이터레이터는 next() 함수를 통해 파일의 각 줄을 순서대로 반환해야 합니다. 파일의 모든 줄을 반환한 후에는 StopIteration 예외를 발생시켜야 합니다.
# - 파일을 열고 닫는 관리는 적절히 처리되어야 합니다.

def file_line_iterator(file_path):
    class FileLineIterator:
        def __init__(self, file_path):
            self.file_path = file_path
            self.file = open(file_path, 'r')
            self.lines = self.file.readlines()
            self.index = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.index < len(self.lines):
                result = self.lines[self.index]
                self.index += 1
                return result
            else:
                self.file.close()
                raise StopIteration

    return FileLineIterator(file_path)


# 예제 파일을 생성하고 테스트해 보겠습니다.
with open('example.txt', 'w') as f:
    f.write("First line\n")
    f.write("Second line\n")
    f.write("Third line\n")

# 파일 경로를 입력하여 이터레이터를 생성하고 사용합니다.
iterator = file_line_iterator('example.txt')

for line in iterator:
    print(line, end='')  # 줄바꿈 문자 포함된 그대로 출력

# 파일 닫힘 여부 확인
print("\n파일이 제대로 닫혔는지 확인:", iterator.file.closed)
