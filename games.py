from deck import Deck, Player

class Makao():
    special_ranks = ('two', 'three', 'four', 'jack', 'queen', 'king', 'ace')

    def __init__(self):
        self.table = []
        self.players = []
        self.number_of_players = 0
        self.deck = Deck(self.table)
    def add_player(self, name):
        self.players.append(Player(self.deck, self.table, name))
        self.number_of_players += 1
    def start_game(self):
        for i in range(5):
            for player in self.players:
                player.draw_card()
        while True:
            self.deck.card_on_table()
            if self.table[-1][0] not in Makao.special_ranks:
                break
    def getstats(self):
        print(self.deck)
        for player in self.players:
            print(player.getname(), player.show_hand())
        print(self.table)

#zwykła wojna dla 2 graczy (wersja automatyczna)
class Wojna():
    suit = ('hearts', 'spades', 'diamond', 'clubs')
    ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace')
    suit_values = (2, 3, 1, 0)
    rank_values = range(2, 15)

    def __init__(self):
        self.table = []
        self.players = []
        self.number_of_players = 0
        self.deck = Deck(self.table)
        self.rounds_played = 0

    def boldness(self):
        for player in self.players:
            #print(player.getsize())
            if player.getsize() == 0:
                return True
        return False

    def add_player(self, name):
        self.players.append(Player(self.deck, self.table, name))
        self.number_of_players += 1

    def start_game(self):
        while self.deck.__sizeof__()+1 > len(self.players):
            for player in self.players:
                player.draw_card()

    def round(self):
        self.rounds_played += 1
        for player in self.players:
            player.shuffle()
            player.card_on_table(0)
        value_p1 = (Wojna.rank_values[Wojna.ranks.index(self.table[-2][0])], Wojna.suit_values[Wojna.suit.index(self.table[-2][1])])
        value_p2 = (Wojna.rank_values[Wojna.ranks.index(self.table[-1][0])], Wojna.suit_values[Wojna.suit.index(self.table[-1][1])])
        #print(value_p1, value_p2)
        if value_p1[0] == value_p2[0]:
            if value_p1[1] > value_p2[1]:
                winner = 0
            else:
                winner = 1
        elif value_p1[0] > value_p2[0]:
            winner = 0
        else:
            winner = 1
        self.players[winner].add_points(1)
        self.players[winner].take_table()

    def getstats(self):
        for player in self.players:
            print(player.getname(), player.getscore())
        if self.players[0].getscore() > self.players[1].getscore():
            print(self.players[0].getname(), 'wins')
        else:
            print(self.players[1].getname(), 'wins')


    def round_number(self):
        return self.rounds_played


wojna = Wojna()
wojna.add_player('emoboi')
wojna.add_player('mareczek')
wojna.start_game()
while not wojna.boldness():
    if wojna.rounds_played > 10000:
        break
    wojna.round()
wojna.getstats()