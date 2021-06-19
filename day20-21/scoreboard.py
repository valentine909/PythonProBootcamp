from turtle import Turtle
from settings import SETTINGS

HEIGHT = SETTINGS['height']


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.color('white')
        self.score = -1
        self.pu()
        self.goto(0, HEIGHT // 2 - 20)
        self.pd()
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align='center', font=("Arial", 14, "bold"))
