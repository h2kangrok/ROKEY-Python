# MARK: 문제 10
# 10.	다음 책에 대한 정보를 저장한 딕셔너리에 대해 다음과 같이 출력하는 프로그램을 작성하라.

books = {"파이썬 개론": ["홍길동"],
         "Perfect C": ["김영수", "이동준"],
         "컴퓨터 개론": ["최환수", "주용호", "박해성"]}


def print_author():

    try:
        name = input("책 이름: ")
        author = books[name]
        print(f"저자: {', '.join(author)}")

    except KeyError:
        print("책이 존재하지 않습니다.")


print_author()
