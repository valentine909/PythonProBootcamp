def game_over():
    print('You\'ve died')
    exit()


def underline(some_text):
    return '\u0332'.join(some_text+" ").strip()


def another_underline(some_text):
    return '\033[4m' + some_text + '\033[0m'


print("Welcome to Treasure Island.\nYour mission is to find the treasure.\n")
print("Enter underlined commands to win the game.\n")
left = another_underline("left")
right = another_underline("right")
direction = input(f"You are on a crossroad. Turn {left} or {right}?: ")
if direction.lower() == "left":
    pass
else:
    game_over()
wait = another_underline("Wait")
swim = another_underline("swim")
decision = input(f"You've came to the river. {wait} for a boat or {swim} across?: ")
if decision.lower() == "wait":
    pass
else:
    game_over()
blue = another_underline("Blue")
red = another_underline("red")
yellow = another_underline("yellow")
door_choice = input(f"You\'re in the room with three doors. Which door will you open? "
                    f"{blue}, {red}, or {yellow}?")
if door_choice.lower() == "yellow":
    print("\nCongrats! You win!")
else:
    game_over()
