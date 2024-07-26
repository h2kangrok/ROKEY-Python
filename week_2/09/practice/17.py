# MARK: 문제 17

def copy_file():
    source_file = input("복사할 원본 파일 이름을 입력하세요: ")
    destination_file = input("새 파일 이름을 입력하세요: ")

    try:
        with open(source_file, 'r', encoding='utf-8') as src:
            with open(destination_file, 'w', encoding='utf-8') as dest:
                content = src.read()
                dest.write(content)
        print(f"{source_file} 파일이 성공적으로 {destination_file} 파일로 복사되었습니다.")
    except FileNotFoundError:
        print(f"파일 {source_file}을(를) 찾을 수 없습니다.")
    except Exception as e:
        print(f"파일을 복사하는 동안 오류가 발생했습니다: {e}")


copy_file()
