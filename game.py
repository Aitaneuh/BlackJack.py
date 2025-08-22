from deck import Deck
from player import Player
from dealer import Dealer

class Game:
    def __init__(self, player: Player, dealer: Dealer) -> None:
        self.player = player
        self.dealer = dealer
        self.deck = Deck()
        self.deck.shuffle()

    def play_round(self):
        self.player.add_card(self.deck.draw())
        self.player.add_card(self.deck.draw())

        self.dealer.add_card(self.deck.draw())
        self.dealer.add_card(self.deck.draw())

        self.player.play(self.dealer.hand[0])

        # TODO Logic for the game