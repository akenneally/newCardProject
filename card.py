import random

class Value:

class Suit:

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

    def get_card(self):



