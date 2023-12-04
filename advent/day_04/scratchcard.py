from collections import deque

from typing import Sequence, List

class Card:

    number: int
    winners: List[int] = []
    scorers: List[int] = []

    def __init__(self, line: str):
        parts = line.split('|')
        number, winners = parts[0].split(':')
        self.number = int(number.split()[1])
        self.winners = list(int(w) for w in winners.split())
        self.scorers = list(int(s) for s in parts[1].split())

    def score(self):
        score = 0
        for number in self.scorers:
            if number in self.winners:
                score = max(1, score * 2)
        return score

    def matching(self):
        score = 0
        for number in self.scorers:
            if number in self.winners:
                score += 1
        return score



def answer_1(lines: Sequence[str]):
    cards = [Card(line) for line in lines]
    return sum(card.score() for card in cards)


def answer_2(lines: Sequence[str]):
    cards = list(Card(line) for line in lines)

    counts = [1] * len(cards)
    for card in cards:
        for index in range(card.number, card.matching() + card.number):
            counts[index] += counts[card.number - 1]

    return sum(counts)
