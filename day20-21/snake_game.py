"""
TO DO steps
1. Create a snake body
2. Move the snake
3. Control the snake
4. Detect collision with food
5. Create a scoreboard
6. Detect collision with wall
7. Detect collision with tail
"""
from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from settings import SETTINGS
WIDTH = SETTINGS['width']
HEIGHT = SETTINGS['height']
SNAKE_MOVE_DELAY = SETTINGS['move_delay']


def init_screen():
    global screen
    screen = Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)


def enable_keys():
    screen.onkey(key='a', fun=snake.to_the_left)
    screen.onkey(key='d', fun=snake.to_the_right)


def main():
    global snake
    init_screen()
    screen.update()
    snake = Snake()
    food = Food()
    score = Scoreboard()
    enable_keys()
    screen.listen()
    game_is_on = True
    while game_is_on:
        snake.move_forward()
        screen.update()
        if snake.head.distance(food) <= 15:
            food.move()
            snake.add_segment()
            score.refresh_score()
        sleep(SNAKE_MOVE_DELAY)


if __name__ == '__main__':
    main()
    screen.mainloop()
