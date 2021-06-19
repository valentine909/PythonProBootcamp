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


def is_food_collision():
    return snake.head.distance(food) <= 15


def is_wall_collision():
    x = WIDTH // 2 - 20
    y = HEIGHT // 2 - 20
    return snake.head.xcor() > x or snake.head.xcor() < -x or snake.head.ycor() > y or snake.head.ycor() < -y


def is_self_collision():
    for segment in snake[1:]:
        if snake.head.distance(segment) < 10:
            return True
    return False


def main():
    global snake, food
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
        if is_food_collision():
            food.move()
            snake.add_segment()
            score.refresh_score()
        if is_wall_collision() or is_self_collision():
            game_is_on = False
            score.game_over()
        sleep(SNAKE_MOVE_DELAY)


if __name__ == '__main__':
    main()
    screen.mainloop()
