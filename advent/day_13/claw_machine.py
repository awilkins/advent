from __future__ import annotations

from typing import Sequence, List
import re

from advent.util import get_resource_cache_path


X_Y = re.compile(r".*X.(\d+), Y.(\d+)")

Vector = tuple[int, int]
Coord = tuple[int, int]


class ClawGame:
    button_a: Vector
    button_b: Vector
    prize: Coord

    def __init__(self, button_a: Vector, button_b: Vector, prize: Coord):
        self.button_a = button_a
        self.button_b = button_b
        self.prize = prize

    def solve(self):
        for aa in range(100):
            for bb in range(100):
                x = (self.button_a[0] * aa) + (self.button_b[0] * bb)
                y = (self.button_a[1] * aa) + (self.button_b[1] * bb)
                if (x, y) == self.prize:
                    return (aa * 3) + bb
        return 0


def generate_machines(lines):
    line_i = iter(lines)
    try:
        while line_1 := next(line_i):
            match_1 = X_Y.match(line_1)
            assert match_1 is not None
            a, b = match_1.groups()
            button_a = (int(a), int(b))

            line_2 = next(line_i)
            match_2 = X_Y.match(line_2)
            assert match_2 is not None
            button_b = tuple(int(n) for n in match_2.groups())
            a, b = match_2.groups()
            button_b = (int(a), int(b))

            line_3 = next(line_i)
            match_3 = X_Y.match(line_3)
            assert match_3 is not None
            prize = tuple(int(n) for n in match_3.groups())
            a, b = match_3.groups()
            prize = (int(a), int(b))

            yield ClawGame(button_a, button_b, prize)
            next(line_i)

    except StopIteration:
        return


def machines(lines):
    m_g = generate_machines(lines)
    return list(m_g)


def answer_1(lines: Sequence[str]):
    ms = machines(lines)
    return sum(m.solve() for m in ms)


def answer_2(lines: Sequence[str]):
    pass
