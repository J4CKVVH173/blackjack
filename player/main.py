from constants import GOLDEN_SCORE


class Player:
    """Instance of a player."""

    __slots__ = ('name', 'score', 'hand')

    def __init__(self, name, score=0):
        self.name = name
        self.score = score
        self.hand = []

    def add_card(self, card):
        """Добавляет карту в руку игрока."""
        self.hand.append(card)

    def add_score(self):
        """Добавляет очки игроку."""
        self.score += 1

    def clear_hand(self):
        """Clear the hand."""
        self.hand.clear()

    def reduce_score(self):
        """Reduce score."""
        self.score -= 1

    def get_hands_value(self) -> int:
        """Return value of the card in the hand."""
        if not self.hand:
            return 0
        values = self._hand_values()
        values.sort()

        for i, val in enumerate(values):
            if val == GOLDEN_SCORE:
                return val
            if val > GOLDEN_SCORE:
                if i == 0:
                    return val
                return values[i - 1]

        return values[-1]

    def _hand_values(self, idx=0, current_value=0) -> list[int]:
        """Calc all possible sums of the hand."""
        if current_value > GOLDEN_SCORE:
            return [current_value]

        if idx >= len(self.hand):
            return [current_value]

        result = []
        for value in self.hand[idx].value:
            result.extend(self._hand_values(idx + 1, current_value + value))

        return result

    def __str__(self):
        return f'{self.name}: {self.score} - {", ".join(map(str, self.hand)) if self.hand else 'Empty'}'
