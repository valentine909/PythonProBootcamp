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
WIDTH = 600
HEIGHT = 600
SNAKE_MOVE_DELAY = 0.3


if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)
    snake = Snake()
    screen.update()
    screen.listen()
    screen.onkey(key='a', fun=snake.to_the_left)
    screen.onkey(key='d', fun=snake.to_the_right)
    game_is_on = True
    while game_is_on:
        snake.move_forward()
        screen.update()
        sleep(SNAKE_MOVE_DELAY)
    screen.exitonclick()
