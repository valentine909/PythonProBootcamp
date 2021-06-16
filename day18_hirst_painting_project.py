from day18_determine_colors import SPECTRA
from turtle import Turtle, Screen, colormode
import random

WIDTH = 800
HEIGHT = 600
STEP = 40
DOT_SIZE = 20


def draw_hirst(drawer: Turtle):
    for j in range(STEP // 2, int(HEIGHT * 1.25), STEP):
        drawer.pu()
        drawer.setposition(-int(WIDTH * 0.625), -int(HEIGHT * 0.625) + j)
        drawer.pd()
        for i in range(STEP // 2, int(WIDTH * 1.25), STEP):
            drawer.dot(DOT_SIZE, random.choice(SPECTRA))
            drawer.pu()
            drawer.forward(STEP)
            drawer.pd()


if __name__ == '__main__':
    screen = Screen()
    screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT)
    t = Turtle()
    t.speed('fastest')
    t.hideturtle()
    colormode(255)
    draw_hirst(t)
    screen.exitonclick()
