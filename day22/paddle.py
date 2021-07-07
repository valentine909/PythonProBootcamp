from turtle import Turtle
from settings import SETTINGS

WIDTH = SETTINGS['width']
HEIGHT = SETTINGS['height']


class Paddle(Turtle):
    def __init__(self, player='first'):
        super().__init__(shape='square')
        self.pu()
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.player = player
        if self.player == 'first':
            self.pos_coeff = 1
        elif self.player == 'second':
            self.pos_coeff = -1
        self.goto((30 - WIDTH // 2) * self.pos_coeff, 0)

    def move_up(self):
        if self.ycor() < HEIGHT // 2 - 55:
            self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -HEIGHT // 2 + 60:
            self.goto(self.xcor(), self.ycor() - 20)

    def check_intersection(self, other_x, other_y):
        if (other_x * self.pos_coeff <= self.pos_coeff * (self.xcor() + 20 * self.pos_coeff)) \
                and (self.ycor() - 60 <= other_y <= self.ycor() + 60):
            return True
        return False
