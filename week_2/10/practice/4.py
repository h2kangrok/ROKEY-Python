# MARK: 문제 4

#  문제4) 다음 요구사항을 코드로 작성한다.
# - 먼저 파일 이름을 입력 받는다.
# - 파일이 없다면 파일 이름을 다시 입력 받고 파일의 내용을 화면에 출력한다.
# - 재 입력한 파일도 없다면 sys.exit() 함수를 이용해서 프로그램을 종료시킨다.
# - 재 입력한 파일이 없다는 오류는 FileNotFoundError를 확인한다.

import sys


def found_file():
    try:
        found_file_name = input("파일 이름을 입력하세요: ")
        with open(found_file_name, "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("파일이 존재하지 않습니다!")
        raise


try:
    found_file()
except FileNotFoundError:
    try:
        found_file()
    except FileNotFoundError:
        print("두 번째 시도에도 파일이 존재하지 않아 프로그램을 종료합니다.")
        sys.exit()
