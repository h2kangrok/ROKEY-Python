# MARK: 문제 11
# 문제11) 문제8번과 같은 방식으로 간단한 내용을 가지는 data2.txt 파일을 생성한다.
# 그 두 파일의 내용을 모두 리스트로 만들고, 리스트를 연결해서 새로운 리스트를 생성한다.
# 새로 만들어진 리스트의 내용을 세 번째 파일에 저장하는 코드를 작성하시오

# data2.txt 파일 생성
with open("data2.txt", "w", encoding="utf-8") as f:
    f.write("\nHello Everyone!")

with open("data.txt", "r", encoding="utf-8") as f:
    data1 = f.readlines()

with open("data2.txt", "r", encoding="utf-8") as f:
    data2 = f.readlines()

combine_list = data1 + data2

with open("combine_data.txt", "w", encoding="utf-8") as f:
    for line in combine_list:
        f.write(line)

with open("combine_data.txt", "r", encoding="utf-8") as f:
    print(f.read())
