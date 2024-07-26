import turtle


def draw_rainbow_circle():
    screen = turtle.Screen()
    screen.bgcolor("black")
    rainbow = turtle.Turtle()
    rainbow.speed(0)
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    radius = 50

    for color in colors:
        rainbow.color(color)
        rainbow.circle(radius)
        radius += 10

    rainbow.hideturtle()
    screen.mainloop()


draw_rainbow_circle()
