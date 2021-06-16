from turtle import Turtle, Screen
import random


def random_hex_color_code():
    """
    :return: random color code like #FFFFFF
    """
    return "#%06x" % random.randint(0, 0xFFFFFF)


def draw_square(drawer: Turtle, length: int):
    for _ in range(4):
        drawer.forward(length)
        drawer.right(90)


def draw_dash(drawer: Turtle, step: int, times: int):
    for _ in range(times):
        drawer.pd()
        drawer.forward(step)
        drawer.pu()
        drawer.forward(step)


def draw_polygon(drawer: Turtle, side_length: int, number_of_sides: int):
    for _ in range(number_of_sides):
        angle = 360 / number_of_sides
        drawer.forward(side_length)
        drawer.right(angle)


def draw_shapes():
    turtle.width(3)
    turtle.pu()
    turtle.goto(-100, 100)
    turtle.pd()
    print(turtle.pos())
    for _ in range(3, 10):
        color = random_hex_color_code()
        turtle.color(color)
        draw_polygon(turtle, 100, _)


def random_walk(drawer: Turtle):
    turtle.width(5)
    turtle.speed(9)
    angles = [0, 90, 180, 270]
    for _ in range(300):
        turtle.color(random_hex_color_code())
        drawer.forward(20)
        drawer.setheading(random.choice(angles))


def draw_spirograph(drawer: Turtle):
    drawer.speed(0)
    drawer.width(2)
    for _ in range(0, 360, 5):
        drawer.setheading(_)
        drawer.color(random_hex_color_code())
        drawer.circle(100)


turtle = Turtle()
turtle.shape('arrow')
# draw_square(turtle, 100)
# draw_dash(turtle, 10, 15)
# draw_polygon(turtle, 200, 9)
# draw_shapes()
# random_walk(turtle)
draw_spirograph(turtle)
screen = Screen()
screen.exitonclick()
