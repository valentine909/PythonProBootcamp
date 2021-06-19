from turtle import Turtle
from random import randrange
from settings import SETTINGS

WIDTH = SETTINGS['width']
HEIGHT = SETTINGS['height']


class Food(Turtle):
    def __init__(self):
        super(Food, self).__init__(shape='circle')
        self.color('blue')
        self.pu()
        self.speed("fastest")
        self.move()

    def move(self):
        x_boundary = WIDTH // 2
        y_boundary = HEIGHT // 2
        random_x = randrange(-x_boundary + 40, x_boundary - 40, 20)
        random_y = randrange(-y_boundary + 40, y_boundary - 40, 20)
        self.goto(random_x, random_y)
