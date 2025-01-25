from deck.card.main import Card
from .. import Player


def test_adding_cards():
    """Test adding cards to a hand."""
    player = Player('gost')
    card = Card.build_card()
    player.add_card(card)
    assert player.hand == [card]


def test_checks_score():
    """Test checks score of a hand."""
    player = Player('gost')

    card1 = Card.build_card(name='ace')
    player.add_card(card1)
    assert player.get_hands_value() == 11

    card2 = Card.build_card(name='two')
    player.add_card(card2)
    assert player.get_hands_value() == 13

    card3 = Card.build_card(name='jack')
    player.add_card(card3)
    assert player.get_hands_value() == 13
