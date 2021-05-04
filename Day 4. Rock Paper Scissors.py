from day4source import *
GAME_DICT = {0: rock,
             1: paper,
             2: scissors,
             }


def player_choice() -> int:
    choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
    try:
        print(f"You chose:\n{GAME_DICT[choice]}")
    except KeyError:
        print("Provide correct input")
        choice = player_choice()
    return choice


def comp_choice() -> int:
    import random
    choice = random.randrange(0, 3)
    print(f"Computer chose:\n{GAME_DICT[choice]}")
    return choice


def try_again() -> bool:
    choice = input("Play again? Type Y(y) or N(n): ").lower()
    if choice == 'y':
        return True
    else:
        return False


def game(pl_choice: int, c_choice: int):
    victory = [(1, 0), (2, 1), (0, 2)]
    if (pl_choice, c_choice) in victory:
        print("You win!")
    elif pl_choice == c_choice:
        print("Draw")
    else:
        print("You lose")


if __name__ == '__main__':
    again = True
    while again:
        game(player_choice(), comp_choice())
        again = try_again()
    print("Goodbye")
