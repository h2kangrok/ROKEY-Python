# MARK: 문제 6
# 6.	원을 그리고, 원의 내부는 빨간색으로 채우시오. 그리고 원의 외곽선은 파랑색으로 그리는 프로그램을 작성하시오.

import turtle as t

t.pencolor("blue")
t.fillcolor("red")

t.begin_fill()
t.circle(100)
t.end_fill()

t.mainloop()
