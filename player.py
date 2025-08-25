from card import Card

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.hand = []

    def play(self, dealer_card: Card) -> str:
        dealer_hand_value = self.get_hand_value([dealer_card])
        hand_value = self.get_hand_value(self.hand)
        is_soft = self.contains_ace_as_eleven(self.hand)

        if is_soft:
            return self.soft_strategy(hand_value, dealer_hand_value)
        else:
            return self.hard_strategy(hand_value, dealer_hand_value)
    
    def add_card(self, card: Card) -> None:
        self.hand.append(card)

    def get_hand_value(self, hand):
        hand_value = 0
        aces_count = 0
        for card in hand:
            if card.type in ["Jack","Queen","King"]:
                hand_value += 10
            elif card.type == "Ace":
                aces_count += 1
            else:
                if isinstance(card.type, int):
                    hand_value += card.type
        for i in range(aces_count):
            if hand_value < 11:
                hand_value += 11
            else:
                hand_value += 1
        return hand_value
    
    def contains_ace_as_eleven(self, hand: list) -> bool:
        value = 0
        aces = 0
        for card in hand:
            if card.type in ["Jack","Queen","King"]:
                value += 10
            elif card.type == "Ace":
                aces += 1
            else:
                value += int(card.type)

        value += aces
        if aces > 0 and value + 10 <= 21:
            return True
        return False

    def hard_strategy(self, value: int, dealer: int) -> str:
        if value <= 11:
            return "hit"
        if 12 <= value <= 16:
            if 2 <= dealer <= 6:
                return "stand"
            else:
                return "hit"
        else:
            return "stand"

    def soft_strategy(self, value: int, dealer: int) -> str:
        if value <= 17:
            return "hit"
        if value == 18:
            if 2 <= dealer <= 8:
                return "stand"
            else:
                return "hit"
        else:
            return "stand"