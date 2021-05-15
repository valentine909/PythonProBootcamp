import os
from day10_art import logo
OPERATIONS = ['+', '-', '*', '/']


def greetings():
    print(logo)


def check_input(number: str) -> bool:
    """
    Checks if the input can be evaluated as a number
    :param number: string
    :return: True or False
    """
    try:
        number = float(number)
    except ValueError:
        return False
    return True


def main(n1):
    print(*OPERATIONS, sep='\n')
    operator = input("Pick an operator from the line above:")
    n2 = input("What's the next number?: ")
    if all(map(check_input, (n1, n2))) and operator in OPERATIONS:
        answer = eval(n1 + operator + n2)
        print(f"{n1} {operator} {n2} = {answer}")
        return str(answer)
    else:
        print("Invalid input")
        exit()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def calculator():
    number1 = input("What's the first number?: ")
    while True:
        ans = main(number1)
        continue_repeat_exit = input(f"Type 'y' to continue calculating with {ans}, type 'n' to start a new "
                                     f"calculation, or anything else to exit: ")
        if continue_repeat_exit == 'y':
            number1 = ans
            continue
        elif continue_repeat_exit == 'n':
            clear()
            calculator()
            break
        else:
            print("Goodbye")
            break


if __name__ == '__main__':
    greetings()
    calculator()
