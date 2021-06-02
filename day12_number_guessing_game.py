import random
from day12_art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randrange(1, 101)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0
if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5
else:
    print("Wrong input!")
    exit()
while attempts:
    print(f"You have {attempts} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    attempts -= 1
    if guess == number:
        print("You win!")
        print(f"The number was {number}")
        exit()
    elif guess > number:
        print("Too high.\nGuess again.")
    else:
        print("Too low.\nGuess again.")
print("You lose!")
print(f"The number was {number}")
