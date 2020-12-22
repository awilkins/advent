
from collections import deque
from typing import List, Tuple


def score(deck: deque[int]) -> int:
    count = 0
    value = 0
    while len(deck) > 0:
        card = deck.pop()
        count += 1
        value += card * count

    return value


def play_round(player1: deque[int], player2: deque[int]):

    card1 = player1.popleft()
    card2 = player2.popleft()

    if card1 > card2:
        player1.append(card1)
        player1.append(card2)

    if card2 > card1:
        player2.append(card2)
        player2.append(card1)


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
        play_round(player1, player2)

    winning_deck = [deck for deck in [player1, player2] if len(deck) > 0][0]

    return score(winning_deck)
