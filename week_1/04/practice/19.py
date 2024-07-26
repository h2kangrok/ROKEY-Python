# MARK: 문제 19
# 문제 19번

interest = input("관심도 (없음, 조금, 보통, 많음, 매우 많음 중 하나) : ")
efforts = input("노력도 (상, 중, 하 중 하나) : ")

if interest in ["보통", "많음", "매우 많음"]:
    if efforts == "상":
        print("예비 파이썬 고수")
    elif efforts == "중":
        print("예비 파이썬 중수")
    elif efforts == "하":
        print("노력 필요")
    else:
        print("노력도 입력이 잘못되었습니다.")
elif interest in ["없음", "조금"]:
    print("파이썬에 대해 관심을 가져 보세요.")
else:
    print("관심도 입력이 잘못되었습니다.")
