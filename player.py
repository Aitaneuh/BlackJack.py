class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.hand = []

    def play(self, dealer_card) -> str:
        # TODO strat algo
        return 'stand'