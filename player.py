from card import Card

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.hand = []

    def play(self, dealer_card: Card) -> str:
        # TODO strat algo
        return 'stand'
    
    def add_card(self, card: Card) -> None:
        self.hand.append(card)
    
    def get_hand_value(self):
        hand_value = 0
        for card in self.hand:
            hand_value += card.value
        return hand_value