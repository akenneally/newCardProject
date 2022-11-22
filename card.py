import random

class Value:
    pass

class Suit:
    pass

class Card:
    def __init__(self, value, suit):
        self.cardValue = value
        self.cardSuit = suit


class Deck:
    def __init__(self):
        self.cards = []

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def create_deck(self):
        for suit in range (1, 5):
            for value in range (1, 14):
                new_card = Card(value, suit)
                self.cards.append(new_card)


    def get_card(self):



