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
    def __init__(self):
        self.hand = []

    def draw(self):
        import random
        self.hand.append(random.choice(CARDS))

    def show_cards(self):
        return self.hand

    def score(self):
        score = sum(self.hand)
        if score > 21 and 11 in self.hand:
            self.hand.remove(11)
            self.hand.append(1)
        return sum(self.hand)


class Computer(Player):
    def show_cards(self, full=False):
        return self.hand if full else self.hand[0]


class Blackjack:
    def __init__(self, AI=Computer(), Human=Player()):
        self.AI = AI
        self.Human = Human

    def start(self):
        print(logo)
        self.Human.hand = []
        self.AI.hand = []
        for i in range(2):
            self.Human.draw()
            self.AI.draw()
        self.current_table()
        self.game()

    def calculation_of_results(self, final=False):
        if final:
            if self.AI.score() > 21 or self.Human.score() > self.AI.score():
                return self.win()
            elif self.Human.score() < self.AI.score():
                return self.lose()
            else:
                return self.draw()
        if self.Human.score() > 21:
            return self.lose()
        elif self.Human.score() == 21 and self.AI.score() == 21:
            return self.draw()
        elif self.Human.score() == 21:
            return self.win()
        return False

    def win(self):
        self.final_table()
        print("You Win")
        return True

    def lose(self):
        self.final_table()
        print("You Lose")
        return True

    def draw(self):
        self.final_table()
        print("Draw")
        return True

    def current_table(self):
        print(f"Your cards: {self.Human.show_cards()}, current score: {self.Human.score()}")
        print(f"Computer's first card: {self.AI.show_cards()}")

    def final_table(self):
        print(f"Your final hand: {self.Human.show_cards()}, final score: {self.Human.score()}")
        print(f"Computer's final hand: {self.AI.show_cards(full=True)}, final score: {self.AI.score()}")

    def game(self):
        proceed = input("Type 'y' to get another card, type 'n' to pass: ")
        while proceed == 'y':
            self.Human.draw()
            if self.calculation_of_results():
                return
            self.current_table()
            proceed = input("Type 'y' to get another card, type 'n' to pass: ")
        if self.calculation_of_results():
            return
        while self.AI.score() < 17 and not self.AI.score() > 21:
            self.AI.draw()
        self.calculation_of_results(final=True)


if __name__ == '__main__':
    is_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    while is_playing == 'y':
        game_session = Blackjack()
        game_session.start()
        is_playing = input("Do you want to play more? Type 'y' or 'n': ")
