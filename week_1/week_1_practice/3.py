# 3-21)
# 한 줄의 문자열을 입력으로 받아, 문자열의 한 문자를 참조하는 코드를 아래와 같은 방식으로 작성해 본다.
# - 16은 문자열의 길이: len함수를 이용함 (ex: length = len('문자열')
# - 문자열 내의 한 문자 참조: 문자열[index]

# 문자열을 입력 >> Python is great!
# 참조하고 싶은 문자의 위치 입력 (0 ~ 16) >> 2
# 문자열: Python is great!, 길이: 16
# 3번째 문자 : t

s = input("문자열을 입력하세요. : ")
num = int(input("참조하고 싶은 문자의 위치 입력(0 ~ 16) : "))

length = len(s)
char = s[num]

print(f"문자열: {s}, 길이: {length}")
print(f"{num+1}번째 문자 : {char}")
