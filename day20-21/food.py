from turtle import Turtle
from random import randint
from settings import SETTINGS

WIDTH = SETTINGS['width']
HEIGHT = SETTINGS['height']


class Food(Turtle):
    def __init__(self):
        super(Food, self).__init__(shape='circle')
        self.color('blue')
        self.pu()
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.move()

    def move(self):
        x_boundary = WIDTH // 2
        y_boundary = HEIGHT // 2
        random_x = randint(-x_boundary + 20, x_boundary - 20)
        random_y = randint(-y_boundary + 20, y_boundary - 20)
        self.goto(random_x, random_y)
