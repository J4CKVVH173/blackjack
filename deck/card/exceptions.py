class UnknownCardValue(Exception):
    """404 analog to UnknownCardValue."""

    def __init__(self, card):
        super().__init__(f'Unknown card value: {card}')
