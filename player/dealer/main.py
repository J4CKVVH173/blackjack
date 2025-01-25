from deck.card import Card

from deck import Deck
from player import Player
from .exceptions import DeckIsMissed


class Dealer(Player):
    """
    Particular player.

    Dealer is a special type of player who plays against the players.
    """

    __slots__ = 'deck'

    deck: Deck | None

    def __init__(self, *args, **kwargs):
        super().__init__(name='dealer', *args, **kwargs)
        self.deck = None

    def set_deck(self, deck: Deck):
        """Set a new deck."""
        deck.shuffle()
        self.deck = deck

    def ask_card(self) -> Card:
        """Request a card."""
        if not self.deck:
            raise DeckIsMissed()
        return self.deck.pop()

    def make_move(self):
        """Dealer plays."""
        while self.get_hands_value() < 17:
            self.add_card(self.ask_card())
