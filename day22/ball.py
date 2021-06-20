from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.color('white')
        self.pu()
        self.speed('slowest')

    def move(self):
        self.forward(10)

    def start_over(self):
        self.goto(0, 0)
        self.setheading(0)
