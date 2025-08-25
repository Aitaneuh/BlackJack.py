from player import Player

class Dealer(Player):
    def play(self, dealer_card=None) -> str:
        total = self.get_hand_value(self.hand)
        return 'hit' if total < 17 else 'stand'