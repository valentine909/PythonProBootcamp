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
from random import randint
from turtle import Screen, Turtle
from time import sleep
from settings import SETTINGS
from ball import Ball
from player import Player

WIDTH = SETTINGS['width']
HEIGHT = SETTINGS['height']
BACKGROUND_COLOR = SETTINGS['bgcolor']
TITLE = SETTINGS['title']
GAME_SPEED = SETTINGS['delay']

global screen, ball, player_one, player_two


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
    screen.onkeypress(key='w', fun=player_one.paddle.move_up)
    screen.onkeypress(key='s', fun=player_one.paddle.move_down)
    screen.onkeypress(key='Up', fun=player_two.paddle.move_up)
    screen.onkeypress(key='Down', fun=player_two.paddle.move_down)


def is_wall_collision():
    y = HEIGHT // 2 - 10
    return ball.ycor() > y or ball.ycor() < -y


def is_ball_escaped_player_one():
    x = WIDTH // 2 - 10
    return ball.xcor() < -x


def is_ball_escaped_player_two():
    x = WIDTH // 2 - 10
    return ball.xcor() > x


def is_paddle_collision():
    if player_one.paddle.check_intersection(ball.xcor(), ball.ycor()) or \
            player_two.paddle.check_intersection(ball.xcor(), ball.ycor()):
        ball.move_speed *= 0.9
        return True
    else:
        return False


def main():
    global ball, player_one, player_two, game_speed
    init_screen()
    ball = Ball()
    player_one = Player(name='first')
    player_two = Player(name='second')
    screen.update()
    enable_keys()
    screen.listen()
    game_is_on = True
    while game_is_on:
        ball.move()
        screen.update()
        if is_wall_collision():
            ball.setheading(360 - ball.heading())
        if is_ball_escaped_player_one():
            player_two.score.refresh_score()
            ball.start_over(True)
        if is_ball_escaped_player_two():
            player_one.score.refresh_score()
            ball.start_over()
        if is_paddle_collision():
            ball.setheading((180 - ball.heading() + randint(-45, 45)) % 360)
        sleep(GAME_SPEED * ball.move_speed)


if __name__ == '__main__':
    main()
    screen.mainloop()
