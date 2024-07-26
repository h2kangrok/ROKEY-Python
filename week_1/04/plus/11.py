# MARK: 문제 11
# 문제 11번

num = int(input("4자리 정수를 입력하시오 : "))

if num < 1000 or num > 9999:
    print("잘못 입력하셨습니다. 4자리 연도를 입력해주세요.")

else:
    print("첫 두자리 : ", num // 100)
    print("마지막 두자리 : ", num % 100)
