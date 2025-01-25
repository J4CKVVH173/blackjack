from copy import deepcopy
import pytest

from .. import Deck
from ..exceptions import NoMoreCards


def test_deck_initialization():
    """Test checks initialization of a deck."""
    deck = Deck()
    assert len(deck.cards) == 52


def test_compares_deck_after_shuffle():
    """Test checks if deck is equal after shuffle."""
    deck1 = Deck()
    deck2 = deepcopy(deck1)
    deck1.shuffle()
    assert deck1 != deck2


def test_checks_getting_card():
    """Test check getting card from deck."""
    deck = Deck()
    top_card = deepcopy(deck.cards[-1])
    card = deck.pop()

    assert card == top_card


def test_getting_more_then_52():
    """Test check getting more then 52 cards."""
    deck = Deck()
    for _ in range(52):
        deck.pop()

    with pytest.raises(NoMoreCards) as _:
        deck.pop()
