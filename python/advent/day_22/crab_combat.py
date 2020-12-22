
from collections import deque
from itertools import islice

from hashlib import new, sha1


from typing import List, Set, Tuple


def score(deck: deque[int]) -> int:
    count = 0
    value = 0
    deck.reverse()
    for card in deck:
        count += 1
        value += card * count
    deck.reverse()

    return value


def play_combat_round(player1: deque[int], player2: deque[int]):

    card1 = player1.popleft()
    card2 = player2.popleft()

    if card1 > card2:
        player1.append(card1)
        player1.append(card2)

    if card2 > card1:
        player2.append(card2)
        player2.append(card1)


class RecursiveCombat:

    def __init__(self, player1: deque[int], player2: deque[int]):
        self.player1 = player1
        self.player2 = player2
        self.previous_positions: Set[bytes] = set([])


    def hash_position(self) -> bytes:
        position = sha1(usedforsecurity=False)

        for card in self.player1:
            position.update(card.to_bytes(length=1, byteorder='little'))

        for card in self.player2:
            position.update(card.to_bytes(length=1, byteorder='little'))

        return position.digest()


    def play_round(self) -> int:
        """ returns 0 for continue, 1 for player1 wins, etc """

        position = self.hash_position()
        if position in self.previous_positions:
            return 1

        self.previous_positions.add(position)

        card1 = self.player1.popleft()
        card2 = self.player2.popleft()

        if card1 <= len(self.player1) and card2 <= len(self.player2):
            # Play a recursive game
            new_player_1 = deque(islice(self.player1, card1))
            new_player_2 = deque(islice(self.player2, card2))
            new_game = RecursiveCombat(new_player_1, new_player_2)
            recursive_winner = new_game.play()
            if recursive_winner == 1:
                self.player1.append(card1)
                self.player1.append(card2)
            else:
                self.player2.append(card2)
                self.player2.append(card1)
        else:
            # Fall back to non-recursive play
            if card1 > card2:
                self.player1.append(card1)
                self.player1.append(card2)

            if card2 > card1:
                self.player2.append(card2)
                self.player2.append(card1)

        if len(self.player1) == 0:
            return 2
        if len(self.player2) == 0:
            return 1

        return 0


    def play(self) -> int:
        winner = 0
        while winner == 0:
            winner = self.play_round()

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

    if winner == 1:
        return score(game.player1), game
    if winner == 2:
        return score(game.player2), game

    return 0, game
