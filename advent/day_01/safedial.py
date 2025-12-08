from __future__ import annotations

from typing import Sequence, List


def rotate(position, command):
    vector = 0
    if command[0] == "R":
        vector += 1
    elif command[0] == "L":
        vector -= 1

    scalar = int(command[1:])

    clicks = 0

    new_position = position
    for _ in range(scalar):
        new_position = (new_position + vector) % 100
        if new_position == 0:
            clicks += 1

    return new_position, clicks


def silent_click():
    pass


class Safe:
    dial = 50
    clicks = 0

    def __init__(self, position=50):
        self.dial = position

    def rotate(self, command):
        self.dial, clicks = rotate(self.dial, command)
        self.clicks += clicks
        return self.dial


def answer_1(lines: Sequence[str]):
    safe = Safe()
    positions = [safe.rotate(command) for command in lines]
    zeroes = sum(1 for position in positions if position == 0)
    return zeroes


def answer_2(lines: Sequence[str]):
    safe = Safe()
    for command in lines:
        safe.rotate(command)
    return safe.clicks
