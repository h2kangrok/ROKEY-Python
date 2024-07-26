# MARK: 문제 12

def classify_roots(a, b, c):

    delta = b**2 - 4 * a * c

    if delta > 0:
        return "해는 실수이고 2개의 다른 값이 존재함"
    elif delta == 0:
        return "해는 실수이고 1개 값만 존재함"
    else:
        return "해는 복소수이고 2개의 다른 값이 존재함"


a = float(input("이차 방정식의 계수 a를 입력하세요: "))
b = float(input("이차 방정식의 계수 b를 입력하세요: "))
c = float(input("이차 방정식의 계수 c를 입력하세요: "))

print(classify_roots(a, b, c))
