
from collections import deque
from itertools import chain, islice

from pathlib import Path


from typing import List, Set, Tuple

from tests.util import get_resource


def score(deck: deque[int]) -> int:
    count = 0
    value = 0
    deck.reverse()
    for card in deck:
        count += 1
        value += card * count
    deck.reverse()

    return value


log: List[str] = []
game_count = 0

class RecursiveCombat:

    def __init__(self, player1: deque[int], player2: deque[int]):
        global game_count
        game_count += 1
        log.append(f"=== Game {game_count} ===")

        self.game = game_count
        self.round_count = 0

        self.player1 = player1
        self.player2 = player2
        self.previous_positions: Set[bytes] = set([])


    def hash_position(self) -> bytes:
        position = bytes(chain(self.player1, [0], self.player2))
        return position


    def play_round(self) -> int:
        """ returns 0 for continue, 1 for player1 wins, etc """

        self.round_count += 1
        log.append("")
        log.append(f"-- Round {self.round_count} (Game {self.game}) --")
        log.append(f"Player 1's deck: {', '.join(str(i) for i in self.player1)}")
        log.append(f"Player 2's deck: {', '.join(str(i) for i in self.player2)}")

        position = self.hash_position()
        if position in self.previous_positions:
            log.append(f"Player 1 wins round {self.round_count} of game {self.game} by recursion!")
            return 1

        self.previous_positions.add(position)

        card1 = self.player1.popleft()
        log.append(f"Player 1 plays: {card1}")
        card2 = self.player2.popleft()
        log.append(f"Player 2 plays: {card2}")

        if card1 <= len(self.player1) and card2 <= len(self.player2):
            # Play a recursive game
            new_player_1 = deque(islice(self.player1, card1))
            new_player_2 = deque(islice(self.player2, card2))
            log.append("Playing a sub-game to determine the winner...")
            log.append("")
            new_game = RecursiveCombat(new_player_1, new_player_2)
            recursive_winner = new_game.play()
            log.append(f"...anyway, back to game {self.game}.")
            if recursive_winner == 1:
                self.player1.append(card1)
                self.player1.append(card2)
                log.append(f"Player 1 wins round {self.round_count} of game {self.game}!")
            elif recursive_winner == 2:
                self.player2.append(card2)
                self.player2.append(card1)
                log.append(f"Player 2 wins round {self.round_count} of game {self.game}!")
            else:
                raise RuntimeError("THERE CAN BE ONLY ONE")
        else:
            # Fall back to non-recursive play
            if card1 > card2:
                self.player1.append(card1)
                self.player1.append(card2)
                log.append(f"Player 1 wins round {self.round_count} of game {self.game}!")
            elif card2 > card1:
                self.player2.append(card2)
                self.player2.append(card1)
                log.append(f"Player 2 wins round {self.round_count} of game {self.game}!")
            else:
                raise RuntimeError("EQUAL CARDS")

        winner = 0
        if len(self.player1) == 0:
            winner = 2
        if len(self.player2) == 0:
            winner = 1

        return winner


    def play(self) -> int:
        winner = 0
        while winner == 0:
            winner = self.play_round()

        log.append(f"The winner of game {self.game} is player {winner}!")
        log.append("")
        return winner


def parse(lines: List[str]) -> Tuple[deque[int], deque[int]]:

    deck1: deque[int] = deque()
    ii = 1
    line = lines[ii]
    while len(line) > 0:
        deck1.append(int(line))
        ii += 1
        line = lines[ii]

    ii += 2
    deck2: deque[int] = deque()
    while ii < len(lines):
        line = lines[ii]
        deck2.append(int(line))
        ii += 1

    return deck1, deck2


def play_combat_round(player1: deque[int], player2: deque[int]):

    card1 = player1.popleft()
    card2 = player2.popleft()

    if card1 > card2:
        player1.append(card1)
        player1.append(card2)

    if card2 > card1:
        player2.append(card2)
        player2.append(card1)


def play_combat(lines: List[str]) -> int:

    player1, player2 = parse(lines)
    while len(player1) > 0 and len(player2) > 0:
        play_combat_round(player1, player2)

    winning_deck = [deck for deck in [player1, player2] if len(deck) > 0][0]

    return score(winning_deck)


def play_recursive_combat(lines: List[str]) -> Tuple[int, RecursiveCombat]:

    player1, player2 = parse(lines)
    game = RecursiveCombat(player1, player2)
    winner = game.play()

    log.append("")
    log.append("== Post-game results ==")
    log.append(f"Player 1's deck: {', '.join(str(i) for i in game.player1)}".rstrip())
    log.append(f"Player 2's deck: {', '.join(str(i) for i in game.player2)}".rstrip())
    if winner == 1:
        return score(game.player1), game
    if winner == 2:
        return score(game.player2), game

    return 0, game


def main():
    DAY = "22"
    input_lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
    answer, game = play_recursive_combat(input_lines)
    print(f'\nAnswer 2 : {answer}\n')
    print(game.player1)
    print(game.player2)

    with Path('/tmp/log.txt').open('w') as file:
        for line in log:
            file.write(line)
            file.write("\n")

    assert 34746 < answer



if __name__ == "__main__":
    main()
