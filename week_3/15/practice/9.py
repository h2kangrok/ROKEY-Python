# MARK: 문제 9

# 9.	키보드의 방향키(화살표)를 누르면 거북이가 화살표 방향으로 이동하면서 선을 그리는 프로그램을 작성하라.
# - 위, 아래 화살표를 누르면 전진, 후진하면서 선을 그린다.
# - 오른쪽, 왼쪽 화살표를 누르면 우방향, 좌방향으로 회전하면서 선을 그린다
# <참조함수>
# - turtle.pendown() 현재 위치에 도장을 찍어 선을 그림
# - turtle.right(5) 오른쪽으로 5도 회전 : turtle.left(5) 왼쪽으로 5도 회전
# - t.Screen().onkeypress(move_forward, "Up")  키보드 이벤트 처리 / 위쪽 화살표 키
# - t.Screen().onkeypress(move_backward, "Down")  아래쪽 화살표 키
# - t.Screen().onkeypress(move_right, "Right")  오른쪽 화살표 키
# - t.Screen().onkeypress(move_left, "Left")  왼쪽 화살표 키

import turtle as t

# 거북이 설정
turtle = t.Turtle()
turtle.speed(0)  # 가장 빠른 속도로 설정

# 이동 함수 정의


def move_forward():
    turtle.pendown()
    turtle.forward(10)


def move_backward():
    turtle.pendown()
    turtle.backward(10)


def turn_right():
    turtle.right(5)


def turn_left():
    turtle.left(5)


# 화면 설정
screen = t.Screen()
screen.listen()  # 키보드 이벤트 리스닝 시작

# 키보드 이벤트에 함수 바인딩
screen.onkeypress(move_forward, "Up")
screen.onkeypress(move_backward, "Down")
screen.onkeypress(turn_right, "Right")
screen.onkeypress(turn_left, "Left")

# 이벤트 루프 시작
t.mainloop()
