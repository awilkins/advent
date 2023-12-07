from __future__ import annotations

from typing import Sequence, Dict

CARD_VALUES = [ 'A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2' ]
JOKER_CARDS = CARD_VALUES.copy()
CARD_VALUES.reverse()

del JOKER_CARDS[3]
JOKER_CARDS.append('J')
JOKER_CARDS.reverse()

def card_key(c, jokers_wild = False):
    if jokers_wild :
        return JOKER_CARDS.index(c)
    return CARD_VALUES.index(c)

HAND_CLASSES = [
    FIVE := [5],
    FOUR := [4, 1],
    FULL_HOUSE := [3, 2],
    THREE := [3, 1, 1],
    TWO_PAIR := [2, 2, 1],
    PAIR := [2, 1, 1, 1],
    HIGH := [1, 1, 1, 1, 1],
]
HAND_CLASSES.reverse()


def hand_class(hand, jokers_wild = False):
    cards: Dict[str, int] = {}
    for card in hand:
        cards[card] = cards.get(card, 0) + 1

    if jokers_wild and 'J' in hand:
        joker_count = cards['J']
        if joker_count < 5:
            del cards['J']
            remaining_cards = [(count, card) for card, count in cards.items()]
            remaining_cards.sort(key = lambda x : x[0])
            remaining_cards.reverse()
            equal_remaining_cards = [card for count, card in remaining_cards if count == remaining_cards[0][0]]
            equal_remaining_cards.sort(key=card_key)
            equal_remaining_cards.reverse
            most = equal_remaining_cards[-1]
            cards[most] += joker_count

    run_lengths = list(cards.values())
    run_lengths.sort()
    run_lengths.reverse()
    return run_lengths

def hand_key(hand, jokers_wild = False):
    key = []
    key.append(str(
        HAND_CLASSES.index(hand_class(hand, jokers_wild))
    ))
    for card in hand:
        key.append(hex(card_key(card, jokers_wild))[-1])
    return int(
        "".join(key), 16
    )

def hand_bid_key(handbid, jokers_wild = False):
    hand = handbid[0]
    return hand_key(hand, jokers_wild)

def winnings(lines, jokers_wild = False):
    hands = []
    for line in lines:
        parts = line.split()
        cards = parts[0]
        bid = int(parts[1])
        hands.append(
            (cards, bid)
        )

    hands.sort(key=lambda x : hand_bid_key(x, jokers_wild))

    winnings = sum(
        (index + 1) * bid for index, (_, bid) in enumerate(hands)
    )
    return winnings

def answer_1(lines: Sequence[str]):
    return winnings(lines)

def answer_2(lines: Sequence[str]):
    return winnings(lines, True)
