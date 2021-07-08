import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

global screen, player


def enable_keys():
    screen.onkeypress(key='w', fun=player.move_up)


def setup_screen():
    global screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.title('Turtle Crossing Game')
    screen.tracer(0)


def main():
    global player
    difficulty_coefficient = 1.0
    setup_screen()
    player = Player()
    score = Scoreboard()
    manager = CarManager()
    enable_keys()
    screen.listen()
    game_is_on = True
    while game_is_on:
        manager.create_car()
        manager.move_cars()
        if manager.collision_with_car(player):
            score.game_over()
            game_is_on = False
        if player.cross_the_finish_line():
            player.restart()
            score.update_level()
            difficulty_coefficient *= 0.95
        time.sleep(0.1 * difficulty_coefficient)
        screen.update()


if __name__ == '__main__':
    main()
    screen.mainloop()
