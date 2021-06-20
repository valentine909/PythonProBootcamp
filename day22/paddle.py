from turtle import Turtle
from settings import SETTINGS

WIDTH = SETTINGS['width']
HEIGHT = SETTINGS['height']


class Paddle(Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.pu()
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(WIDTH // 2 - 30, 0)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
