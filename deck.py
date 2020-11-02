import random
from itertools import product


class Deck():
    suit = ('hearts', 'spades', 'diamond', 'clubs')
    ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight',
             'nine', 'ten', 'jack', 'queen', 'king', 'ace')

    def __init__(self):
        self.deck1 = list(product(Deck.ranks, Deck.suit))
        random.shuffle(self.deck1)
    def draw_card(self):
        if len(self.deck1) == 0:
            raise Exception('Deck empty!')
        else:
            card = self.deck1[-1][0] +' of ' +self.deck1[-1][1]
            self.deck1.pop()
            return card
    def shuffle_deck(self):
        random.shuffle(self.deck1)
    def __str__(self):
        return str(self.deck1)
    def getsize(self):
        return len(self.deck1)


deck1 = Deck()
hand = []
for i in range(52):
    hand.append(deck1.draw_card())
print(hand)

