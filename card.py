import random


class Card:
    value = None
    suit = None

    def __init__(self, value, suit):
        self.cardValue = value
        self.cardSuit = suit

    def __str__(self):
        return 'Card Value: {}, Card Suit: {}'.format(self.value, self.suit)


class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck
        self.shuffle_deck
        self.get_card


card = Card("Card", 3)
card.__str__()
