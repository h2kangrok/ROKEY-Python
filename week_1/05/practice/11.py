# 문제11) 4. 세 개의 16진수로 구성된 문자열을 입력 받고, 정수 십진수로 변환해서 화면에 출력하는 프로그램을 작성한다.
# 예: 입력 내용이 "A9E"라면 10 * 256 + 9 * 16 + 14의 결과값인 2718을 출력한다.


s = input("세 개의 16진수로 구성된 문자열을 입력하세요. : ")
print(int(s, 16))
