# MARK: 문제 5

f = open("data.txt", "w")
data = "Hello\nThis is data.txt\n이 파일은 utf-8 형식으로 저장했습니다\n"
f.write(data)
f.close()

print(data)

with open("data,txt", "w", encoding="utf-8") as f:
    data = "Hello\nThis is data.txt\n이 파일은 utf-8 형식으로 저장했습니다\n"
    f.write(data)

with open("data.txt", "r", encoding="utf-8") as f:
    line = f.readline()
    print(line)
