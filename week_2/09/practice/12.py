# MARK: 문제 12
# 문제12) 검색할 문자열을 입력받아,
# 문제15에서 새로 만들어진 파일에서 검색하고 몇 번째 라인에 있는지 보여주는 코드를 작성해 본다.

def find_str_in_file():
    while True:
        try:
            s = input("검색할 문자열을 입력하세요 ex) 0.4 or 0.43 : ")

            with open("data3.txt", "r", encoding="utf-8") as f:
                data_list = f.read().strip().split()
                print(data_list)

            found = False
            for idx, line in enumerate(data_list):
                if s in line:
                    print(f"'{s}' 문자열을 찾았습니다. {idx + 1}번째 라인에 있습니다.")
                    found = True
                    break

            if not found:
                print(f"'{s}' 문자열을 파일에서 찾을 수 없습니다.")

        except FileNotFoundError:
            print("파일을 찾을 수 없습니다. 'data3.txt' 파일이 존재하는지 확인하세요.")
            break


find_str_in_file()
