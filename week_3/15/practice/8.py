# MARK: 문제 8
# 8.	이 코드는 각 반복에서 터틀이 91도씩 왼쪽으로 회전하면서 선을 그리는 예제입니다.
# colors[i % 4]를 사용하여 색상을 순환하면서 그립니다.
# 프로그램을 실행해서 어떤 도형이 그려지는지 확인해 보세요.

import turtle
turtle.speed(0)  # 숫자가 클수록 빠르게 그립니다. 0는 가장 빠른 속도입니다.
turtle.bgcolor("black")  # 배경색
colors = ["red", "yellow", "blue", "green"]
for i in range(100):
    turtle.color(colors[i % 4])  # colors 인덱스를 만들어 색상을 순환시킵니다.
    turtle.forward(i * 4)  # 현재 반복 횟수 i에 4를 곱한 만큼 앞으로 전진합니다.
# 이로 인해 반복할 때마다 그리는 선의 길이가 점점 길어집니다.
    turtle.left(91)
turtle.done()
