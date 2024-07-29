# MARK: 문제 5
# 5.	아래의 코드를 람다함수의 형식으로 변환하시오
# <주의사항>
# - 람다함수에서 사용하는 조건부 표현식에는 :(콜론)을 사용하지 않음
# - 람다함수에서 if를 사용하면 반드시 else를 사용해야 함
# - 람다함수에서 elif는 사용하지 못함

def checkNum(x):
    if x < 3:
        return x
    elif x < 6:
        return x * 2
    else:
        return x * 3


numbers = [2, 3, 4, 5, 6, 7]
result = map(checkNum, numbers)
print(list(result))

print(list(map(lambda x: x if x < 3 else x * 2 if x < 6 else x * 3, numbers)))
