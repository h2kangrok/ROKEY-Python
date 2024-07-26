# MARK: 문제 9
# 문제9) 존재하지 않는 파일을 읽으려 할 때 발생하는 예외를 처리하고,
# 파일이 성공적 으로 읽혔는지 여부에 따라 메시지를 출력하세요.
# - try, except(file not found), else, finally 블록을 사용할 것

def solution():
    try:
        found_file_name = input("검색할 파일 이름을 입력하세요: ")
        with open(found_file_name, "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("파일이 존재하지 않습니다.")
    else:
        print("파일을 성공적으로 읽었습니다.")
    finally:
        print("예외처리가 잘되었습니다.")


solution()
