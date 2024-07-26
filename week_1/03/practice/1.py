# MARK: 문제 1
# 문제1) 3. 반지름 5인 원의 면적을 계산할 때. 5 x 5 x 3.14 로 계산하는 코드는 반지름이 바뀔 때마다
# 코드를 수정해야 하므로 좋지 않다. 어떻게 프로그래밍하는 것이 효율적일까?
def solution(radius):
    pi = 3.14
    area = pi * (radius**2)
    return area


print(solution(5))
