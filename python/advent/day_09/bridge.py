
from __future__ import annotations
from typing import List, Tuple


def clamp(x):
    return -1 if x < -1 else 1 if x > 1 else x


class Rope:

    head: Tuple[int, int]
    tail: Tuple[int, int]
    label: str
    next: "Rope" | None

    moves = dict(
        U = (0, -1),
        D = (0, 1),
        L = (-1, 0),
        R = (1, 0),
    )

    tail_log = []

    def __init__(self, knot_count=2, tail_start=(0,0)):
        self.head = (0,0)
        self.tail = tail_start
        self.tail_log = [self.tail]
        knot_count -= 1
        if knot_count > 1:
            self.next = Rope(knot_count, self.tail)
        else:
            self.next = None


    def move(self, direction):
        mx, my = self.moves[direction]
        x, y = self.head
        self.head = (x + mx, y + my)


    def follow(self):
        hx, hy = self.head
        tx, ty = self.tail

        dx = hx - tx
        dy = hy - ty

        if max(abs(x) for x in [dx, dy]) < 2: return

        dx = clamp(dx)
        dy = clamp(dy)

        self.tail = (tx + dx, ty + dy)
        self.tail_log.append(self.tail)
        if self.next:
            self.next.head = self.tail
            self.next.follow()


    def end(self):
        return self.next.end() if self.next else self


def moves(lines: List[str]):
    bits = [line.split(' ') for line in lines]
    return [ (bit[0], int(bit[1])) for bit in bits ]


def answer_1(lines: List[str]):

    rope = Rope(2)
    for direction, count in moves(lines):
        for _ in range(count):
            rope.move(direction)
            rope.follow()

    return len(set(rope.tail_log))


def answer_2(lines: List[str]):
    rope = Rope(10)
    for direction, count in moves(lines):
        for _ in range(count):
            rope.move(direction)
            rope.follow()

    return len(set(rope.end().tail_log))

