# 문제 16번

def solution():
    for n1 in range(1, 10):
        for n2 in range(1, 10):
            if int(str(n1)+str(n2)) + int(str(n1)+str(n2)) == 110:
                print(f"n1 : {n1}, n2 : {n2}")


solution()


def solution():
    for n1 in range(1, 10):
        for n2 in range(1, 10):
            if n1 + n2 == 10:
                print(f"n1 : {n1}, n2 : {n2}")


solution()
