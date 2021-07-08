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
        self.high_score = 0
        self.get_high_score()
        self.pu()
        self.goto(0, HEIGHT // 2 - 30)
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.score += 1
        self.write_text(f"Score: {self.score} High score: {self.high_score}")

    def write_text(self, some_text):
        self.write(some_text, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write_text('Game Over!')

    def save_score(self):
        if self.score > self.high_score:
            with open('score.txt', 'w') as f:
                f.write(str(self.score))

    def get_high_score(self):
        try:
            with open('score.txt', 'r') as f:
                self.high_score = int(f.read())
        except FileNotFoundError:
            self.high_score = 0

    def reset(self):
        self.save_score()
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = -1
        self.refresh_score()
