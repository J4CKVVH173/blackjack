from .. import Card
from ..types import CardName, Suit


def test_card_creating():
    """Test card creation."""
    card = Card(Suit.HEARTS, CardName.ACE)
    assert card.suit == Suit.HEARTS
    assert card.name == CardName.ACE
    assert card.value == [1, 11]
    assert str(card) == '♥ACE'


def test_card_equals():
    """Test card equals."""
    card1 = Card(Suit.HEARTS, CardName.ACE)
    card2 = Card(Suit.HEARTS, CardName.ACE)
    assert card1 == card2


def test_different_cards_equals():
    """Test different cards equals."""
    card1 = Card(Suit.HEARTS, CardName.ACE)
    card2 = Card(Suit.CLUBS, CardName.JACK)
    assert not card1 == card2
