from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape='circle')
        self.color('white')
        self.pu()
        self.speed('fast')
        self.move_speed = 1

    def move(self):
        self.forward(10)

    def start_over(self, reverse=False):
        self.goto(0, 0)
        self.setheading(180 * reverse)
        self.move_speed = 1