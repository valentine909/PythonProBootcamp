from day14_game_data import data
from day14_art import logo, vs
from random import shuffle
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def pop_from_data():
    return data.pop()


def game():
    score = 0
    choice_a = pop_from_data()
    while 1:
        clear()
        print(logo)
        if score > 0:
            print(f"You're right! Your current score is: {score}.")
        print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}.")
        print(vs)
        choice_b = pop_from_data()
        print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}.")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if guess == 'a' and choice_a['follower_count'] > choice_b['follower_count']:
            score += 1
        elif guess == 'b' and choice_b['follower_count'] > choice_a['follower_count']:
            score += 1
            choice_a = choice_b
        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Your final score is: {score}.")
            return


if __name__ == '__main__':
    shuffle(data)
    game()
