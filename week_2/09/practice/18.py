# MARK: 문제 18

# 문제18) 문법상 오류가 없는 파이썬 코드 파일을 읽고, 주석문을 제거한 코드를 다른 파일에 저장하는 프로그램을 작성한다.
# 원본 코드 파일 이름은 사용자로부터 입력 받고, 새로 저장되는 코드의 파일 이름은 원본 파일이름 앞에 "new_"를 붙인다.

def remove_comments_from_file():
    # 사용자로부터 원본 파일 이름을 입력받음
    source_file = input("주석을 제거할 원본 파이썬 코드 파일 이름을 입력하세요: ")

    # 새 파일 이름 생성
    destination_file = "new_" + source_file

    try:
        # 원본 파일을 읽기 모드로 엶
        with open(source_file, 'r', encoding='utf-8') as src:
            lines = src.readlines()

        # 주석을 제거한 내용을 저장할 리스트
        lines_without_comments = []

        # 각 줄을 검사하여 주석을 제거
        for line in lines:
            stripped_line = line.strip()
            # 주석으로 시작하는 줄은 무시
            if stripped_line.startswith('#'):
                continue
            # 주석이 포함된 줄 처리 (간단한 형태만 처리)
            elif '#' in stripped_line:
                line = line.split('#')[0].rstrip() + '\n'
            lines_without_comments.append(line)

        # 새 파일을 쓰기 모드로 엶
        with open(destination_file, 'w', encoding='utf-8') as dest:
            dest.writelines(lines_without_comments)

        print(f"{source_file} 파일의 주석이 성공적으로 제거되어 {destination_file} 파일에 저장되었습니다.")
    except FileNotFoundError:
        print(f"파일 {source_file}을(를) 찾을 수 없습니다.")
    except Exception as e:
        print(f"파일을 처리하는 동안 오류가 발생했습니다: {e}")


remove_comments_from_file()
