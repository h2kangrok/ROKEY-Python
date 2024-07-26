# MARK: 문제 11

def discomfort_index(ta, tw):
    DI = 0.72*(ta+tw) + 40.6

    return DI


def comfort_level(DI):
    if DI < 68:
        return "모든 사람이 쾌적함을 느낌"
    elif 68 <= DI < 75:
        return "불쾌감을 나타내기 시작함"
    elif 75 <= DI < 80:
        return "반 정도의 사람이 불쾌감을 느낌"
    else:
        return "모든 사람이 불쾌감을 느낌"


ta = float(input("건구온도를 입력하세요. : "))
tw = float(input("습구온도를 입력하세요. : "))

DI = discomfort_index(ta, tw)

comfort_message = comfort_level(DI)

print(f"불쾌지수: {DI:.2f}")
print(comfort_message)
