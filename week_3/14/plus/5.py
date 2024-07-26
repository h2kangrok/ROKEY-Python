# MARK: 문제 5
# 5.	영한사전과 같이 한글과 영어에 대응되는 튜플 korean과 english를 만든 후,
# 표준입력으로 한글을 입력받아 영어를 출력하는 프로그램을 작성하시오.

korean = ('정렬‘, ’문자’, ‘내포’ , ‘사전')
english = ('sorting', 'text', 'comprehension', 'dictionary')


def solution():
    korean_str = input("힌글을 입력하세요 : ")
    if korean_str in korean:
        print(english[korean.index(korean_str)])
    else:
        print("단어가 사전에 존재하지 않습니다.")


solution()

# korean = ('정렬', '문자', '내포', '사전')
# english = ('sorting', 'text', 'comprehension', 'dictionary')

# def solution():
#     korean_str = input("한글을 입력하세요 : ")
#     if korean_str in korean:
#         print(english[korean.index(korean_str)])
#     else:
#         print("단어가 사전에 존재하지 않습니다.")

# solution()
