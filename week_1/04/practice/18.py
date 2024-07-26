# MARK: 문제 18
# 문제 18번)
import math

h, w = map(float, input("당신의 키(cm)와 몸무게(kg)는? ").split())

bmi = w/pow((h/100), 2)


def result(bmi):
    if bmi >= 40:
        return "고도비만"
    elif 40 > bmi >= 35:
        return "중증도 비만"
    elif 35 > bmi >= 30:
        return "비만"
    elif 30 > bmi >= 25:
        return "과체중"
    elif 25 > bmi >= 18.5:
        return "정상"
    else:
        return "저체중"


print(f"BMI: {bmi:.1f} {result(bmi)}")
