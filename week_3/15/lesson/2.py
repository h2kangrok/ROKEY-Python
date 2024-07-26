import turtle


def draw_star():
    screen = turtle.Screen()
    screen.bgcolor("black")
    star = turtle.Turtle()
    star.speed(1)
    colors = ["red", "yellow", "blue", "green", "purple"]

    for i in range(5):
        star.color(colors[i])
        star.forward(100)
        star.right(144)

    star.hideturtle()
    screen.mainloop()


draw_star()
