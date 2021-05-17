from day11_art import logo
CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Our Blackjack House Rules
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10. Х
# The the Ace can count as 11 or 1.
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.


class Player:
    def __init__(self, ai=True):
        self.ai = ai
        self.hand = []

    def draw(self):
        import random
        self.hand.append(random.choice(CARDS))

    def show_cards(self):
        if self.ai:
            return self.hand[0]
        else:
            return self.hand

    def score(self):
        return sum(self.hand)


print(logo)
beginning = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")


def game():
    print(f"Your cards: {user.show_cards()}, current score: {user.score()}")
    print(f"Computer's first card: {house.show_cards()}")
    decision = input("Type 'y' to get another card, type 'n' to pass: ")


def calculation_of_results():
    print(f"Your final hand: {user.show_cards()}, final score: {user.score()}")
    print(f"Computer's final hand: {}")
    print("You Win")
    print("You Lose")
    print("Draw")


house = Player
user = Player(ai=False)
