from turtle import Turtle, Screen
import random

COLORS = ['red', 'yellow', 'orange', 'green', 'blue', 'purple']
WIDTH = 640
HEIGHT = 480
STEP = 50
TURTLE_SIZE = 1.5


def draw_finish_line():
    turtle = Turtle(visible=False)
    turtle.speed('fastest')
    turtle.width(2)
    turtle.pencolor("red")
    turtle.pu()
    turtle.goto(WIDTH / 2 - TURTLE_SIZE * 40 / 2, -HEIGHT/2)
    turtle.pd()
    turtle.goto(WIDTH / 2 - TURTLE_SIZE * 40 / 2, HEIGHT / 2)


def create_turtles():
    turtles = []
    x_0 = -WIDTH // 2 + TURTLE_SIZE * 20
    y_0 = -HEIGHT // 4
    for count, color in enumerate(COLORS):
        t = Turtle(shape='turtle')
        t.shapesize(TURTLE_SIZE)
        t.color(color)
        t.pu()
        t.setposition(x_0, y_0 + count * STEP)
        turtles.append(t)
    return turtles


def race(competitors):
    is_a_winner_exists = False
    furthest = -WIDTH / 2
    leader = ''
    while not is_a_winner_exists:
        for turtle in competitors:
            turtle.forward(random.randint(20, 40))
            if turtle.xcor() > furthest:
                furthest = turtle.xcor()
                leader = turtle.pencolor()
            if turtle.xcor() > WIDTH / 2 - TURTLE_SIZE * 40:
                is_a_winner_exists = True
    return leader


if __name__ == '__main__':
    screen = Screen()
    screen.title('Turtle Race')
    screen.setup(width=WIDTH, height=HEIGHT)
    draw_finish_line()
    user_bet = screen.textinput(title="Who wins?", prompt='Name a color: ')
    winner = race(create_turtles())
    if user_bet == winner:
        print(f"The winner is {winner}. You win!")
    else:
        print(f"The winner is {winner}. You lose!")
    screen.exitonclick()
