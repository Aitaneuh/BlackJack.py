from deck import Deck
from player import Player
from dealer import Dealer

class Game:
    def __init__(self, player: Player, dealer: Dealer) -> None:
        self.player = player
        self.dealer = dealer
        self.deck = Deck()
        self.deck.shuffle()

    def has_blackjack(self, player: Player) -> bool:
        if player.get_hand_value(player.hand) == 21:
            return True
        return False


    def play_one_game(self):
        self.player.add_card(self.deck.draw())
        self.player.add_card(self.deck.draw())


        self.dealer.add_card(self.deck.draw())
        self.dealer.add_card(self.deck.draw())

        player_blackjack = self.has_blackjack(self.player)
        dealer_blackjack = self.has_blackjack(self.dealer)

        if player_blackjack and not dealer_blackjack:
            return {"outcome":"blackjack", "player_score":21, "dealer_score":self.dealer.get_hand_value(self.dealer.hand), "player_hit_count":0, "dealer_hit_count":0, "score":1}
        elif player_blackjack and dealer_blackjack:
            return {"outcome":"draw", "player_score":21, "dealer_score":21, "player_hit_count":0, "dealer_hit_count":0}
        elif not player_blackjack and dealer_blackjack:
            return {"outcome":"dealer_blackjack", "player_score":self.player.get_hand_value(self.player.hand), "dealer_score":21, "player_hit_count":0, "dealer_hit_count":0, "score":-1}

        player_hit_count = 0
        while True:
            if self.player.play(self.dealer.hand[0]) == 'stand':
                break
            else:
                player_hit_count += 1
                self.player.add_card(self.deck.draw())

            if self.player.get_hand_value(self.player.hand) > 21:
                return {"outcome":"bust", "player_score":self.player.get_hand_value(self.player.hand), "dealer_score":self.dealer.get_hand_value(self.dealer.hand), "player_hit_count":player_hit_count, "dealer_hit_count":0, "score":-1}

        dealer_hit_count = 0
        while True:
            if self.dealer.play() == 'stand':
                break
            else:
                dealer_hit_count += 1
                self.dealer.add_card(self.deck.draw())
            
            if self.dealer.get_hand_value(self.dealer.hand) > 21:
                return {"outcome":"dealer_bust", "player_score":self.player.get_hand_value(self.player.hand), "dealer_score":self.dealer.get_hand_value(self.dealer.hand), "player_hit_count":player_hit_count, "dealer_hit_count":dealer_hit_count, "score":1}
            
        player_hand_value = self.player.get_hand_value(self.player.hand)
        dealer_hand_value = self.dealer.get_hand_value(self.dealer.hand)

        if player_hand_value > dealer_hand_value:
            return {"outcome":"win", "player_score":player_hand_value, "dealer_score":dealer_hand_value, "player_hit_count":player_hit_count, "dealer_hit_count":dealer_hit_count, "score":1}
        elif player_hand_value == dealer_hand_value:
            return {"outcome":"draw", "player_score":player_hand_value, "dealer_score":dealer_hand_value, "player_hit_count":player_hit_count, "dealer_hit_count":dealer_hit_count, "score":0}
        else:
            return {"outcome":"lose", "player_score":player_hand_value, "dealer_score":dealer_hand_value, "player_hit_count":player_hit_count, "dealer_hit_count":dealer_hit_count, "score":-1}