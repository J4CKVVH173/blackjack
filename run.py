"""Run the game."""

from constants import GOLDEN_SCORE
from table import Table
from player.dealer import Dealer
from player import Player
from deck import Deck


if __name__ == '__main__':

    count = None
    dealer = Dealer()
    while count is None:
        command = input('Enter a count of players: ')
        try:
            count = int(command)
        except ValueError:
            count = None

    print()

    players = []

    for i in range(count):
        name = input(f'Enter a name for player {i + 1}: ')
        players.append(Player(name))

    table = Table(dealer, players)

    while True:
        deck = Deck()
        dealer.set_deck(deck)
        table.init_tern()

        for player in table.players:
            print(f'Turn: {player}', end='\n\n')
            while True:
                action = input('Action (hit or stand): ')
                if action == 'hit' or action == 'h':
                    player.add_card(dealer.ask_card())
                    print(' '.join(map(str, player.hand)), player.get_hands_value())
                    hands_value = player.get_hands_value()
                    if hands_value == GOLDEN_SCORE:
                        print('You got 21')
                        break
                    if hands_value > GOLDEN_SCORE:
                        print('You busted')
                        break
                else:
                    break

        dealer.make_move()
        winners = table.check_winners()

        if winners:
            print('Winners:', ', '.join(map(str, winners)))
        else:
            print(f'Dealer wins: {dealer}')

        command = input('Do you want to play again? (yes/no): ')

        if command.lower() != 'yes' or command.lower() != 'y':
            break
