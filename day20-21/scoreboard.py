from turtle import Turtle
from settings import SETTINGS

HEIGHT = SETTINGS['height']
ALIGNMENT = 'center'
FONT = ("Arial", 14, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.color('white')
        self.score = -1
        self.pu()
        self.goto(0, HEIGHT // 2 - 30)
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
