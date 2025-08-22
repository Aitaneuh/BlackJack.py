from player import Player

class Dealer(Player):
    def play(self, dealer_card=None) -> str:
        total = sum(card.value for card in self.hand)
        return 'hit' if total < 17 else 'stand'