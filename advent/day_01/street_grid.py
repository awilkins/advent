from __future__ import annotations

from typing import Sequence, List
from collections import deque

# Starting with north so
vectors = deque(
    [
        (1, 0),  # East
        (0, -1),  # South
        (-1, 0),  # West
    ]
)


class RevisitError(RuntimeError):
    pass


class Dude:
    vectors: deque[tuple[int, int]]
    direction: tuple[int, int]
    position: tuple[int, int]
    visisted: set[tuple[int, int]]
    no_revisit: bool

    def __init__(self, no_revisit=False) -> None:
        self.vectors = deque(vectors)
        self.direction = (0, 1)  # North
        self.position = (0, 0)
        self.visisted = set()
        self.visisted.add(self.position)
        self.no_revisit = no_revisit

    def _move(self, distance):
        for _ in range(distance):
            (dx, dy) = self.direction
            (x, y) = self.position
            self.position = (x + dx, y + dy)
            if self.no_revisit and self.position in self.visisted:
                raise RevisitError()
            self.visisted.add(self.position)

    def move_right(self, distance: int):
        (x, y) = self.position
        self.vectors.append(self.direction)
        self.direction = self.vectors.popleft()
        self._move(distance)

    def move_left(self, distance: int):
        (x, y) = self.position
        self.vectors.appendleft(self.direction)
        self.direction = self.vectors.pop()
        self._move(distance)

    def distance_from_zero(self):
        (x, y) = self.position
        return abs(x) + abs(y)


def answer_1(line: str, no_revisit=False):
    moves = [move.strip("\n ") for move in line.split(",")]
    dude = Dude(no_revisit)
    try:
        for move in moves:
            turn = move[0]
            distance = int(move[1:])
            match turn:
                case "R":
                    dude.move_right(distance)
                case "L":
                    dude.move_left(distance)
    except RevisitError:
        pass
    return dude.distance_from_zero()


def answer_2(line: str):
    return answer_1(line, True)
