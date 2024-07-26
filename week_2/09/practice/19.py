# MARK: 문제 19

# 문제19) 사용자로부터 텍스트 파일 이름을 입력 받고, 파일에 있는 단어 개수를 출력하는 프로그램을 작성한다.
# 단어는 줄바꿈 문자, 탭문자, 공백 문자로 분리된다고 가정한다.

def count_words_in_file():
    # 사용자로부터 파일 이름을 입력받음
    file_name = input("단어 개수를 세고 싶은 텍스트 파일 이름을 입력하세요: ")

    try:
        # 파일을 읽기 모드로 엶
        with open(file_name, 'r', encoding='utf-8') as file:
            # 파일의 내용을 모두 읽음
            content = file.read()

            # 공백, 줄바꿈, 탭 문자로 단어를 분리하여 리스트로 만듦
            words = content.split()

            # 단어의 개수 계산
            word_count = len(words)

            print(f"파일 {file_name}의 단어 개수는 {word_count}개입니다.")
    except FileNotFoundError:
        print(f"파일 {file_name}을(를) 찾을 수 없습니다.")
    except Exception as e:
        print(f"파일을 읽는 동안 오류가 발생했습니다: {e}")


count_words_in_file()
