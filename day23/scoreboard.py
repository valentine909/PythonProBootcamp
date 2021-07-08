from turtle import Turtle

FONT = ("Courier", 20, "bold")
COLOR = 'black'
POSITION = (-280, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.pu()
        self.color(COLOR)
        self.level = 0
        self.goto(POSITION)
        self.update_level()

    def update_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over!', font=FONT, align='center')
