"""
Pong Game
TO DO LIST
1) Playing field
2) Class ball (moving, generation)
3) Class padding
4) Class score
5) Collision with walls
6) Collision with padding
7) Second player
"""
from turtle import Screen, Turtle
from time import sleep
from settings import SETTINGS
from ball import Ball
from score import Scoreboard
from paddle import Paddle

WIDTH = SETTINGS['width']
HEIGHT = SETTINGS['height']
BACKGROUND_COLOR = SETTINGS['bgcolor']
TITLE = SETTINGS['title']
GAME_SPEED = SETTINGS['delay']


global screen, ball, paddle


def draw_central_line():
    liner = Turtle(visible=False)
    liner.color('white')
    liner.pu()
    liner.goto(0, - HEIGHT // 2)
    liner.width(3)
    liner.setheading(90)
    for _ in range(0, HEIGHT, 20):
        liner.pd()
        liner.forward(10)
        liner.pu()
        liner.forward(10)


def init_screen():
    global screen
    screen = Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.bgcolor(BACKGROUND_COLOR)
    screen.title(TITLE)
    screen.tracer(0)
    draw_central_line()


def enable_keys():
    screen.onkeypress(key='w', fun=paddle.move_up)
    screen.onkeypress(key='s', fun=paddle.move_down)


def is_wall_collision():
    y = HEIGHT // 2 - 10
    return ball.ycor() > y or ball.ycor() < -y


def is_ball_escaped():
    x = WIDTH // 2 - 10
    return ball.xcor() > x or ball.xcor() < -x


def is_paddle_collision():
    return ball.distance(paddle) < 40


def main():
    global ball, paddle
    init_screen()
    ball = Ball()
    score = Scoreboard()
    paddle = Paddle()
    screen.update()
    enable_keys()
    screen.listen()
    game_is_on = True
    while game_is_on:
        ball.move()
        screen.update()
        if is_wall_collision():
            ball.setheading((ball.heading() + 180) % 360)
        if is_ball_escaped():
            score.refresh_score()
            ball.start_over()
        if is_paddle_collision():
            ball.setheading((ball.heading() + 180) % 360)
        sleep(GAME_SPEED)


if __name__ == '__main__':
    main()
    screen.mainloop()
