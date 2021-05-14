import os
from day9_art import logo


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


print(logo)
bidders = {}
repeat = True
while repeat:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))
    bidders[name] = bid
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
    if more_bidders == 'yes':
        clear()
    else:
        repeat = False
max_bid = 0
bidder = ''
for _ in bidders:
    if bidders[_] > max_bid:
        max_bid = bidders[_]
        bidder = _
print(f"The winner is {bidder} with a bid of ${max_bid}")
