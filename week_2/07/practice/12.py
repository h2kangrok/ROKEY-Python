# 문제12) 문자열을 매개 변수로 전달 받고, 마침표, 느낌표, 줄바꿈 기호를 제거하는
# 함수를 작성한다. 작성된 함수에 "...What a beautiful day!\n" 문자열을 전달하고 결과값을 받아 화면에 출력하는 프로그램을 구현한다.

def solution(s):
    chars_to_remove = [".", "!", "\n"]

    result = ""

    for char in s:
        if char not in chars_to_remove:
            result += char

    print(result)


solution("...What a beautiful day!\n")
