from turtle import Turtle
from settings import SETTINGS

HEIGHT = SETTINGS['height']
ALIGNMENT = 'center'
FONT = ("Arial", 32, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.color('white')
        self.score = -1
        self.pu()
        self.goto(-30, HEIGHT // 2 - 50)
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.score += 1
        self.write_text(f"{self.score}")

    def write_text(self, some_text):
        self.write(some_text, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write_text('Game Over!')
