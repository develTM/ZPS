import random
from itertools import product


class Deck():
    suit = ('hearts', 'spades', 'diamond', 'clubs')
    ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight',
             'nine', 'ten', 'jack', 'queen', 'king', 'ace')

    def __init__(self):
        self.deck = list(product(Deck.ranks, Deck.suit))
        random.shuffle(self.deck)
    def __str__(self):
        return str(self.deck)
    def __sizeof__(self):
        return len(self.deck)
    def draw_card(self):
        if len(self.deck) == 0:
            raise Exception('Deck empty!')
        else:
            card = self.deck[-1][0], self.deck[-1][1]
            self.deck.pop()
            return card
    def shuffle(self):
        random.shuffle(self.deck)
    def add_card(self, card ):
        self.deck.append(card)

class Hand():
    def __init__(self, deck, table):
        self.deck = deck
        self.table = table
        self.hand = []
    def __str__(self):
        return str(self.hand)
    def __sizeof__(self):
        return len(self.hand)
    def draw_card(self):
        self.hand.append(self.deck.draw_card())
    def card_to_deck(self, n):
        if len(self.hand) < n+1:
            raise Exception('Card index out of range!')
        else:
            self.deck.add_card(self.hand[n])
            del self.hand[n]
    def card_on_table(self, n):
        if len(self.hand) < n+1:
            raise Exception('Card index out of range!')
        else:
            self.table.append(self.hand[n])
            del self.hand[n]


table = []
deck_A = Deck()
hand_1 = Hand(deck_A, table)
hand_2 = Hand(deck_A, table)


hand_1.draw_card()
hand_1.draw_card()
hand_1.card_on_table(0)
for i in range(5):
    hand_2.draw_card()

hand_2.card_to_deck(4)

print(hand_1.__sizeof__() + hand_2.__sizeof__() + len(table) + deck_A.__sizeof__())
