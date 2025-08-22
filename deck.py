from card import Card
import random

class Deck:
    def __init__(self) -> None:
        self.cards = [Card(v,s) for v in range(1,14) for s in ['Hearts','Spades','Diamonds','Clubs']]

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw(self) -> Card:
        return self.cards.pop()