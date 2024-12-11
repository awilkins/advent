from __future__ import annotations

from typing import Deque, Sequence, List
from collections import deque


def blink(pebbles: Deque[int]) -> Deque[int]:
    for _ in range(len(pebbles)):
        top = pebbles[0]
        if top == 0:
            pebbles[0] = 1
        elif len(stop := str(top)) % 2 == 0:
            pebbles[0] = int(stop[(len(stop) // 2) :])
            pebbles.append(int(stop[0 : (len(stop) // 2)]))
        else:
            pebbles[0] = top * 2024
        pebbles.rotate(-1)

    return pebbles


def answer_1(lines: Sequence[str]):
    pebbles = deque(int(n) for n in lines[0].split())
    for _ in range(25):
        pebbles = blink(pebbles)
    return len(pebbles)


def answer_2(lines: Sequence[str]):
    pebbles = deque(int(n) for n in lines[0].split())
    for ii in range(75):
        print(f"{ii} : {len(pebbles)}")
        pebbles = blink(pebbles)
    return len(pebbles)
