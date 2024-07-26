# MARK: 문제 10
# 문제10) 문제8에서 만들어진 파일의 내용을 한 줄씩 읽어서, 새로운 파일을 열어 저장 하는 프로그램을 작성하시오.
# - 새로운 파일의 이름을 입력 받으시오.

new_file_name = input("새로운 파일이 이름을 입력하세요. ex) 영어파일명.txt : ")

with open("data.txt", "r", encoding="utf-8") as f:
    with open(new_file_name, "a", encoding="utf-8") as new_f:
        for line in f:
            new_f.write(line)

with open(new_file_name, "r", encoding="utf-8") as f:
    print(f.read())
