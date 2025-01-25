from random import shuffle

from .card import Card
from .card.types import CardName, Suit
from .exceptions import NoMoreCards


class Deck:
    """Deck of cards."""

    __slots__ = 'cards'

    def __init__(self):
        self.cards = []
        for suit in Suit:
            for name in CardName:
                self.cards.append(Card(suit, name))

    def shuffle(self):
        """Shuffle deck."""
        shuffle(self.cards)

    def pop(self) -> Card:
        """Pop a Card from the deck."""
        if not self.cards:
            raise NoMoreCards('No more cards left in the deck.')
        return self.cards.pop()
