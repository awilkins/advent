
from itertools import pairwise
from collections import deque

from typing import Sequence

NAUGHTINESS = [
    "ab",
    "cd",
    "pq",
    "xy",
]

def contains_naughtiness(line: str):
    for n in NAUGHTINESS:
        if n in line:
            return True
    return False

def contains_three_vowels(line: str):
    vowels = 0
    for c in line:
        if c in 'aeiou':
            vowels += 1
        if vowels == 3:
            return True
    return False

def contains_double_letter(line: str):
    previous_letter = ''
    for c in line:
        if c == previous_letter:
            return True
        previous_letter = c

    return False

def contains_double_couplet(line: str):
    couplets = set(
        ''.join(pair) for pair in pairwise(line)
    )
    for couplet in couplets:
        c_index = line.index(couplet)
        if couplet in line[c_index + 2:]:
            return True
    return False

def contains_blinky_repeat(line: str):
    q = deque('  ', 2)
    for c in line:
        if c == q[0]:
            return True
        q.append(c)


def is_nice(line:str):
    return not contains_naughtiness(line) and contains_three_vowels(line) and contains_double_letter(line)

def is_nicer(line:str):
    return contains_blinky_repeat(line) and contains_double_couplet(line)

def answer_1(lines: Sequence[str]):
    return sum(1 for line in lines if is_nice(line))


def answer_2(lines: Sequence[str]):
    return sum(1 for line in lines if is_nicer(line))
