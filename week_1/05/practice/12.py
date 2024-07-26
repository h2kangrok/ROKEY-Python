# 문제12) ".jpg"로 끝나는 파일 이름을 사용자로부터 입력 받고, ".jpg"를 ".png"로 변환하는 코드를 작성한다.
# replace() 함수를 사용하는 경우와 사용하지 않는 코드 두 개를 작성한다.

s = input("jpg로 끝나는 파일 이름을 입력하세요. : ")

# replace() 사용
print(s.replace("jpg", "png"))
# replace() 사용안함
print(s[:s.find(".")+1] + "png")
