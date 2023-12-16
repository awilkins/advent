from __future__ import annotations

from typing import Sequence, List

def gift_count(house_number: int) -> int:
    gifts = 0
    h = house_number
    # for h in range(1, house_number + 1):
    for e in range(1, h + 1):
        if h % e == 0:
            gifts += e * 10
    return gifts


def house_number(gifts: int):
    g = gift_count(1)
    h = 1

    while g <= gifts:
        h += 1
        g = gift_count(h)

    return h - 1



def answer_1(lines: Sequence[str]):
    return house_number(int(lines[0]))


def answer_2(lines: Sequence[str]):
    pass
