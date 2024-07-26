# 문제8) 주어진 문자열에서 단어의 개수를 세는 함수를 작성하세요. 단어는 공백으로 구분됩니다.


def number_of_words():
    s = input("문자열을 입력하세요. : ").split()
    print(f"{len(s)}개 입니다.")


number_of_words()
