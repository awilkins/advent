from __future__ import annotations

from itertools import pairwise

from collections import deque
from typing import Sequence, List


class OasisLine:

    lines: List[deque[int]]

    def __init__(self, line: str):
        values = deque(int(p) for p in line.split())

        self.lines = []
        self.lines.append(values)

        current_list = values
        while sum(current_list) != 0:
            new_list = deque()
            for a, b in pairwise(current_list):
                new_list.append(b - a)
            self.lines.append(new_list)
            current_list = new_list

    def extend(self):
        prev_line = [0]
        for line in reversed(self.lines):
            line.append(line[-1] + prev_line[-1])
            prev_line = line

    def prepend(self):
        prev_line = [0]
        for line in reversed(self.lines):
            line.appendleft(line[0] - prev_line[0])
            prev_line = line

    def next_value(self):
        return self.lines[0][-1]

    def prev_value(self):
        return self.lines[0][0]


def answer_1(lines: Sequence[str]):
    olines = [OasisLine(line) for line in lines]

    for oline in olines:
        oline.extend()

    return sum(oline.next_value() for oline in olines)


def answer_2(lines: Sequence[str]):
    olines = [OasisLine(line) for line in lines]

    for oline in olines:
        oline.prepend()

    return sum(oline.prev_value() for oline in olines)
