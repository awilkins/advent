from __future__ import annotations

from typing import Sequence, List

def get_lists(lines: Sequence[str]):
    line_pairs = ((int(item) for item in line.split()) for line in lines)
    return [list(t) for t in zip(*line_pairs)]


def answer_1(lines: Sequence[str]):
    one, two = get_lists(lines)

    one.sort()
    two.sort()

    total = 0
    for left, right in zip(one, two):
        total += abs(left - right)

    return total


def item_count(item, list):
    return sum(1 for n in list if n == item)


def answer_2(lines: Sequence[str]):
    list_1, list_2 = get_lists(lines)
    def score(x): return x * item_count(x, list_2)
    return sum([score(x) for x in list_1])

