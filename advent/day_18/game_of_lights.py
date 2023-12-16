from __future__ import annotations

from itertools import chain, product

from typing import Any, Sequence, List, NamedTuple, override

class Position(NamedTuple):
    x: int
    y: int


class World:
    cells: list[list[Light]]

    def __init__(self, lines):
        self.cells = [
            [Light(self, Position(xindex, yindex), c == '#') for xindex, c in enumerate(line)]
            for yindex, line in enumerate(lines)
        ]

    def cell(self, pos: Position):
        return self.cells[pos.y][pos.x]

    def neighbours(self, pos: Position):
        y_range = range(max(pos.y - 1, 0), min(len(self.cells), pos.y + 2))
        x_range = range(max(pos.x - 1, 0), min(len(self.cells[0]), pos.x + 2))
        return [
            self.cell(Position(x, y)) for x, y in product(x_range, y_range)
            if x != pos.x or y != pos.y
        ]

    def lit_neighbours(self, pos: Position):
        return len([light for light in self.neighbours(pos) if light.lit])


    def next_state(self):
        new_world = [
            [l.next_state() for l in row]
            for row in self.cells
        ]
        self.cells = new_world

    def lit_count(self):
        return sum(1 for l in chain.from_iterable(self.cells) if l.lit)

    def __str__(self):
        return "\n".join(
            "".join('#' if l.lit else '.' for l in row)
            for row in self.cells
        )

class Light:

    world: World
    pos: Position

    lit: bool

    def __init__(self, world, pos, lit):
        self.world = world
        self.pos = pos
        self.lit = lit

    def __repr__(self):
        return f"{'#' if self.lit else '.'} ({self.pos.x, self.pos.y})"

    def next_state(self):
        if self.lit:
            if  2 <= self.world.lit_neighbours(self.pos) <= 3:
                return Light(self.world, self.pos, True)
        else:
            if 3 == self.world.lit_neighbours(self.pos):
                return Light(self.world, self.pos, True)
        return Light(self.world, self.pos, False)

class StuckLight(Light):

    def __init__(self, world, pos, lit):
        super().__init__(world, pos, lit)

    @override
    def next_state(self):
        return self

def answer_1(lines: Sequence[str], steps: int):
    world = World(lines)
    for ii in range(steps):
        world.next_state()

    return world.lit_count()

def answer_2(lines: Sequence[str], steps: int):
    world = World(lines)
    world.cells[0][0] = StuckLight(world, Position(0, 0), True)
    world.cells[-1][0] = StuckLight(world, Position(0, 0), True)
    world.cells[0][-1] = StuckLight(world, Position(0, 0), True)
    world.cells[-1][-1] = StuckLight(world, Position(0, 0), True)

    for ii in range(steps):
        world.next_state()

    return world.lit_count()
