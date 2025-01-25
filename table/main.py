from constants import GOLDEN_SCORE
from player.dealer import Dealer
from player import Player


class Table:
    """Game zone."""

    __slots__ = ('players', 'dealer')

    players: list[Player]
    dealer: Dealer

    def __init__(self, dealer: Dealer, players: list[Player]):
        self.players = players
        self.dealer = dealer

    def init_tern(self):
        """All players get two cards in the beginning of the game."""
        self.dealer.clear_hand()
        for player in self.players:
            player.clear_hand()
            for _ in range(2):
                player.add_card(self.dealer.ask_card())

    def check_winners(self) -> list[Player]:
        """Check who won the game."""
        result = []
        dealer_value = self.dealer.get_hands_value()
        for player in self.players:
            player_value = player.get_hands_value()
            if player_value > GOLDEN_SCORE:
                player.reduce_score()
            elif player_value > dealer_value or dealer_value > GOLDEN_SCORE:
                player.add_score()
                result.append(player)

        return result

    def __str__(self):
        return f'{self.dealer}; {" ,".join(map(str, self.players))}'
