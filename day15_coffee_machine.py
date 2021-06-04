from day15_data import MACHINE


def turn_off():
    exit()


def check_resources(name):
    d1 = MACHINE['report']
    d2 = MACHINE[name]
    for key in d2:
        if d1[key] - d2[key] < 0:
            print(f"Sorry, there is not enough {key}.")
            return False
    return True


def print_report():
    d = MACHINE['report']
    print(f"Water: {d['water']} mL\nMilk: {d['milk']} mL\nCoffee: {d['coffee']} g\nMoney: ${d['money']}")


def process_coins(name):
    coins = {'quarters': 0.25, 'dimes': 0.10, 'nickles': 0.05, 'pennies': 0.01}
    cost = MACHINE[name]['money']
    print(f"{name.capitalize()} costs ${-cost}.")
    print("Please insert coins.")
    payment = 0
    for i in coins:
        n = int(input(f"How many {i}: "))
        payment += coins[i] * n
    if payment < -cost:
        print(f"{name.capitalize()} costs ${-cost}. You've inserted ${payment}.")
        print(f"Sorry, that's not enough money. Money refunded.")
        return False
    elif payment > -cost:
        print(f"Here is ${payment + cost} change.")
        return True
    else:
        return True


def make_coffee(name):
    d1 = MACHINE['report']
    d2 = MACHINE[name]
    for key in d2:
        d1[key] -= d2[key]
    print(f"Here is your {name}. Enjoy!")


def order_coffee(order):
    if check_resources(order):
        if process_coins(order):
            make_coffee(order)


COMMANDS = {
    'latte': order_coffee,
    'espresso': order_coffee,
    'cappuccino': order_coffee,
    'off': turn_off,
    'report': print_report,
}


def vending_machine():
    while True:
        order = input("What would you like? (espresso/latte/cappuccino): ")
        if order in ('espresso', 'latte', 'cappuccino'):
            COMMANDS[order](order)
        else:
            COMMANDS[order]()


if __name__ == '__main__':
    vending_machine()
