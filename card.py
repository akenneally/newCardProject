import random


class Card:
    def __init__(self, value, suit):
        self.cardValue = value
        self.cardSuit = suit

    def print_card(self):
        print("The card you have drawn is the {} of {}".format(self.cardValue, self.cardSuit))


class Deck:
    def __init__(self):
        self.cards = []

    def shuffle_deck(self):
        random.shuffle(self.cards)

# create deck of cards

    def create_deck(self):
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
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
drawn_card.print_card()







