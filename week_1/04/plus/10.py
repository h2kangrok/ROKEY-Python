# MARK: 문제 10

year = int(input("연도를 입력해주세요 : "))
month = int(input("월을 입력해주세요 : "))

if year > 0 and 12 >= month >= 1:
    print("True")
else:
    print("False")
