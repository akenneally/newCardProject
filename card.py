import random


class Card:
    def __init__(self, value, suit):
        self.cardValue = value
        self.cardSuit = suit


class Deck:
    def __init__(self):
        self.cards = []

    def shuffle_deck(self):
        random.shuffle(self.cards)

# create deck of cards

    def create_deck(self):
        for suit in ["H", "D", "C", "S"]:
            for value in range(1, 14):
                new_card = Card(value, suit)
                self.cards.append(new_card)

    def print_deck(self):
        for card in self.cards:
            print(card.cardValue, card.cardSuit)

# loop through deck
# print top card
# remove top card from deck
    def get_card(self):
        return self.cards.pop()


new_deck = Deck()
new_deck.create_deck()
new_deck.shuffle_deck()
new_deck.print_deck()
drawn_card = new_deck.get_card()







