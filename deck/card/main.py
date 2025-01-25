from .types import Suit, CardName

from .exceptions import UnknownCardValue


class Card:
    """Card class."""

    __slots__ = ('suit', 'name')

    def __init__(self, suit: Suit, name: CardName):
        self.suit = suit
        self.name = name

    @classmethod
    def build_card(self, suit: str = 'diamonds', name: str = 'ace'):
        """Generate object."""
        suit = Suit[suit.upper()]
        name = CardName[name.upper()]
        return Card(suit, name)

    @property
    def value(self) -> list[int]:
        """Value of the Card."""
        if self.name in [CardName.JACK, CardName.QUEEN, CardName.KING]:
            return [10]
        elif self.name in [
            CardName.TWO,
            CardName.THREE,
            CardName.FOUR,
            CardName.FIVE,
            CardName.SIX,
            CardName.SEVEN,
            CardName.EIGHT,
            CardName.NINE,
            CardName.TEN,
        ]:
            return [self.name.value]
        elif self.name == CardName.ACE:
            return [1, 11]

        raise UnknownCardValue(self.name)

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.suit == other.suit and self.name == other.name

    def __str__(self):
        return f'{self.suit.value} {self.name.name}'

    def __repr__(self):
        return f'<Card: {self.__str__()}>'
