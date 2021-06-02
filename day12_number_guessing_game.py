import random
from day12_art import logo
EASY_LEVEL = 10
HARD_LEVEL = 5


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts = 0
    if difficulty == 'easy':
        attempts = EASY_LEVEL
    elif difficulty == 'hard':
        attempts = HARD_LEVEL
    return attempts


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randrange(1, 101)
    turns = set_difficulty()
    while turns:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        turns -= 1
        if guess == number:
            print("You win!")
            print(f"The number was {number}")
            return
        elif guess > number:
            print("Too high.")
        else:
            print("Too low.")
    print("You lose!")
    print(f"The number was {number}")


if __name__ == '__main__':
    game()
