from __future__ import annotations

from typing import Sequence, List

class Keypad:
    moves: dict[str, tuple[int, int]]
    finger: tuple[int, int]

    def move_finger(self, m):
        (dx, dy) = self.moves[m]
        (x, y) = self.finger
        x = max(0, min(2, x + dx))
        y = max(0, min(2, y + dy))

    def digit_at_finger(self):
        (x, y) = self.finger
        return (x + 1) + (y * 3)


def answer_1(lines: Sequence[str]):
    for line in lines:
        for m in line:



def answer_2(lines: Sequence[str]):
    pass
