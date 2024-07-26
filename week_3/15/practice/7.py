# MARK: 문제 7
# 7.	반지름이 120 이고 원주 각도가 90인 부채꼴 형상의 도형을 그려 보시오.(피자의 1/4조각 같은 모양.)

import turtle as t

# 반지름 설정
radius = 120

# 부채꼴 그리기
t.forward(radius)
t.left(90)
t.circle(radius, 90)
t.left(90)
t.forward(radius)

# 화면이 닫히지 않도록 유지
t.mainloop()
