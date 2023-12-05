from __future__ import annotations

from collections import deque
from itertools import pairwise

from typing import Sequence

def contains_straight(line: Sequence[str]):
    buffer = deque(line[0:2], maxlen=3)

    for c in line[2:]:
        buffer.append(c)
        if ord(buffer[0]) + 2 == ord(buffer[1]) + 1 == ord(buffer[2]):
            return True

    return False


def confusing_chars(line: Sequence[str]):
    return any(bad_char in line for bad_char in 'iol')


def has_enough_pairs(line):

    last_pair = -2
    pair_total = 0
    for index, (a, b) in enumerate(pairwise(line)):
        if a == b and index > last_pair + 1:
            pair_total += 1
            last_pair = index

    return pair_total > 1


def passwords(start:str):

    pword = list(start)

    def increment(sig:int=1):
        new_char = chr(ord(pword[-sig]) + 1)
        if new_char == '{':
            new_char = 'a'
            increment(sig + 1)
        pword[-sig] = new_char

    while True:
        increment()
        if contains_straight(pword) and not confusing_chars(pword) and has_enough_pairs(pword):
            yield "".join(pword)


def answer_1(line: str):
    p = passwords(line)
    return next(p)


def answer_2(line: str):
    p = passwords(line)
    next(p)
    return next(p)
