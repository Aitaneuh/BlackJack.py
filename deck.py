from card import Card
import random

class Deck:
    def __init__(self) -> None:
        self.cards = [Card(v,s) for v in [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"] for s in ['Hearts','Spades','Diamonds','Clubs']]

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw(self) -> Card:
        return self.cards.pop()