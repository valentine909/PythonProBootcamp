from abc import ABCMeta, abstractmethod
"""
Vending Machine project based on Command design pattern.
Receivers: CoffeeMachine, MoneyMachine, Printer, Menu
"""


class CoffeeMachine:
    def __init__(self, water=500, milk=500, coffee=500):
        self.water = water
        self.milk = milk
        self.coffee = coffee

    def add_resources(self, water=0, milk=0, coffee=0):
        self.water += water
        self.milk += milk
        self. coffee += coffee

    def report_resources(self):
        return self.water, self.milk, self.coffee

    def spend_resources(self, water=0, milk=0, coffee=0):
        self.add_resources(-water, -milk, -coffee)

    def turn_off(self):
        exit()


class Printer:
    def print(self, message):
        print(message)


class Drink:
    def __init__(self, name: str, water=0, milk=0, coffee=0, money=0.0):
        self.name = name
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = money

    def get_drink_resources(self):
        return self.water, self.milk, self.coffee

    def get_drink_cost(self):
        return self.money


class Menu:
    def __init__(self):
        self.menu = (
            Drink('latte', water=200, milk=150, coffee=24, money=2.5),
            Drink('espresso', water=50, milk=0, coffee=18, money=1.5),
            Drink('cappuccino', water=250, milk=50, coffee=24, money=3.0),
        )

    def get_all_drinks_name(self):
        return [item.name for item in self.menu]

    def get_drink(self, name: str):
        for drink in self.menu:
            if drink.name == name:
                return drink


class MoneyMachine:
    def __init__(self):
        self.money = 0
        self.COINS = {'quarters': 0.25, 'dimes': 0.10, 'nickles': 0.05, 'pennies': 0.01}

    def take_payment(self):
        payment = 0
        for i in self.COINS:
            n = int(input(f"How many {i}: "))
            payment += self.COINS[i] * n
        self.money += payment
        return payment

    def return_money(self, money):
        self.money -= money

    def get_balance(self):
        return self.money


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass


class MakeCoffee(Command):
    def __init__(self, coffee_machine: CoffeeMachine, printer: Printer):
        self.drink = None
        self.coffee_machine = coffee_machine
        self.printer = printer

    def set_drink(self, drink: Drink):
        self.drink = drink

    def execute(self):
        w, m, c = self.drink.get_drink_resources()
        self.coffee_machine.spend_resources(w, m, c)
        self.printer.print(f"Here is your {self.drink.name}. Enjoy!")


class PrintReport(Command):
    def __init__(self, printer: Printer, coffee_machine: CoffeeMachine):
        self.printer = printer
        self.coffee_machine = coffee_machine

    def execute(self):
        w, m, c = self.coffee_machine.report_resources()
        self.printer.print(f"Water: {w} mL\nMilk: {m} mL\nCoffee: {c} g")


class CheckBalance(Command):
    def __init__(self, printer: Printer, money_machine: MoneyMachine):
        self.printer = printer
        self.money_machine = money_machine

    def execute(self):
        d = self.money_machine.get_balance()
        self.printer.print(f"Money: ${d}")


class TurnOff(Command):
    def __init__(self, coffee_machine: CoffeeMachine):
        self.coffee_machine = coffee_machine

    def execute(self):
        self.coffee_machine.turn_off()


class CheckResources(Command):
    def __init__(self, coffee_machine: CoffeeMachine, printer: Printer):
        self.drink = None
        self.coffee_machine = coffee_machine
        self.printer = printer

    def set_drink(self, drink: Drink):
        self.drink = drink

    def execute(self):
        w1, m1, c1 = self.coffee_machine.report_resources()
        w2, m2, c2 = self.drink.get_drink_resources()
        if w1 - w2 < 0:
            self.printer.print("Not enough water.")
            return False
        elif m1 - m2 < 0:
            self.printer.print("Not enough milk.")
            return False
        elif c1 - c2 < 0:
            self.printer.print("Not enough coffee.")
            return False
        return True


class Payment(Command):
    def __init__(self, money_machine: MoneyMachine, printer: Printer):
        self.money_machine = money_machine
        self.drink = None
        self.printer = printer

    def set_drink(self, drink: Drink):
        self.drink = drink

    def execute(self):
        cost = self.drink.get_drink_cost()
        self.printer.print(f"{self.drink.name.capitalize()} costs ${cost:.2f}.")
        self.printer.print("Please insert coins.")
        income = self.money_machine.take_payment()
        if cost > income:
            print(f"{self.drink.name.capitalize()} costs ${cost:.2f}. You've inserted ${income:.2f}.")
            print(f"Sorry, that's not enough money. Money refunded.")
            return False
        elif income > cost:
            self.printer.print(f"Here is ${(income - cost):.2f} change.")
            self.money_machine.return_money(income - cost)
        return True


class CoffeeMachineInterface:
    def __init__(self, coffee_machine: CoffeeMachine, money_machine: MoneyMachine, menu: Menu, printer: Printer):
        self.order = None
        self.drink = None
        self.coffee_machine = coffee_machine
        self.money_machine = money_machine
        self.menu = menu
        self.printer = printer
        self.turn_off = TurnOff(self.coffee_machine)
        self.pay = Payment(self.money_machine, self.printer)
        self.check_resources = CheckResources(self.coffee_machine, self.printer)
        self.print_report = PrintReport(self.printer, self.coffee_machine)
        self.check_balance = CheckBalance(self.printer, self.money_machine)
        self.make_coffee = MakeCoffee(self.coffee_machine, self.printer)
        self.COMMANDS = {
            'latte': self.order_coffee,
            'espresso': self.order_coffee,
            'cappuccino': self.order_coffee,
            'off': self.turn_off.execute,
            'report': self.report,
        }

    def set_order(self):
        order = input(f"What would you like? ({'/'.join(self.menu.get_all_drinks_name())}): ")
        self.order = order.lower()
        try:
            self.drink = self.menu.get_drink(self.order)
        except Exception as e:
            self.printer.print(e)
        try:
            self.COMMANDS[self.order]()
        except Exception as e:
            self.printer.print(e)

    def order_coffee(self):
        self.check_resources.set_drink(self.drink)
        if self.check_resources.execute():
            self.pay.set_drink(self.drink)
            if self.pay.execute():
                self.make_coffee.set_drink(self.drink)
                self.make_coffee.execute()

    def report(self):
        self.print_report.execute()
        self.check_balance.execute()


if __name__ == '__main__':
    cm = CoffeeMachine(500, 500, 500)
    mm = MoneyMachine()
    p = Printer()
    me = Menu()
    cmi = CoffeeMachineInterface(cm, mm, me, p)
    while True:
        cmi.set_order()
