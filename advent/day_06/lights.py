from __future__ import annotations

from itertools import chain, repeat

from typing import Sequence, Tuple

class Instruction2:

    action: function
    top_left: Tuple
    bottom_right: Tuple

    def do(self, lights):
        top_x, top_y = self.top_left
        btm_x, btm_y = self.bottom_right
        for yy in range(top_y, btm_y + 1):
            for xx in range(top_x, btm_x + 1):
                lights[yy][xx] = self.action(lights[yy][xx])

    def on(self, light):
        return light + 1

    def off(self, light):
        result = light - 1
        return result if result > 0 else 0

    def toggle(self, light):
        return light + 2

    def __init__(self, line):
        parts = line.split()

        if len(parts) == 5:
            del parts[0]

        self.action = getattr(self, parts[0])

        self.top_left = tuple(int(n) for n in parts[1].split(','))
        self.bottom_right = tuple(int(n) for n in parts[-1].split(','))

        assert self.top_left[0] <= self.bottom_right[0]
        assert self.top_left[1] <= self.bottom_right[1]

class Instruction:

    action: function
    top_left: Tuple
    bottom_right: Tuple

    def do(self, lights):
        top_x, top_y = self.top_left
        btm_x, btm_y = self.bottom_right
        for yy in range(top_y, btm_y + 1):
            for xx in range(top_x, btm_x + 1):
                lights[yy][xx] = self.action(lights[yy][xx])

    def on(self, _):
        return 1

    def off(self, _):
        return 0

    def toggle(self, light):
        return 0 if light else 1

    def __init__(self, line):
        parts = line.split()

        if len(parts) == 5:
            del parts[0]

        self.action = getattr(self, parts[0])

        self.top_left = tuple(int(n) for n in parts[1].split(','))
        self.bottom_right = tuple(int(n) for n in parts[-1].split(','))

        assert self.top_left[0] <= self.bottom_right[0]
        assert self.top_left[1] <= self.bottom_right[1]



def answer_1(lines: Sequence[str]):
    lights = []
    for _ in range(1_000):
        lights.append([0] * 1_000)

    instructions = [Instruction(line) for line in lines]
    for instruction in instructions:
        instruction.do(lights)

    return sum(light for light in chain.from_iterable(lights))

def answer_2(lines: Sequence[str]):
    lights = []
    for _ in range(1_000):
        lights.append([0] * 1_000)

    instructions = [Instruction2(line) for line in lines]
    for instruction in instructions:
        instruction.do(lights)

    return sum(light for light in chain.from_iterable(lights))
