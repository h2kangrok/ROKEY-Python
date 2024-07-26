# 문제19) 16진수 색상 코드를 RGB 포맷에 맞게 변환하는 프로그램을 작성하시오.
# 예제: FFA501 -> (255, 165, 1)
# - int(16진수값, 16) : 16진수값을 10진수로 변환하는 함수 참조

def hex_to_rgb(hex):
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))


print(hex_to_rgb("FFA501"))
