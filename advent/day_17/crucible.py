from __future__ import annotations

from collections import deque

from functools import reduce

from typing import Sequence, List, NamedTuple, TypeAlias

class Vector(NamedTuple):
    x: int
    y: int

    def opposite(self):
        if self == DOWN:
            return UP
        if self == RIGHT:
            return LEFT
        if self == LEFT:
            return RIGHT
        if self == UP:
            return DOWN

UP    = Vector( 0, -1)
DOWN  = Vector( 0, +1)
LEFT  = Vector(-1,  0)
RIGHT = Vector(+1,  0)

DIRECTIONS = [ UP, DOWN, LEFT, RIGHT ]

class Position(NamedTuple):
    x: int
    y: int

    def __add__(self, other: Vector) -> Position:
        return Position(
            self.x + other.x,
            self.y + other.y
        )

class City:

    blocks: list[list[int]]

    def __init__(self, lines: Sequence[str]) -> None:
        self.blocks = [
            [int(c) for c in line]
            for line in lines
        ]

    def block(self, pos: Position) -> int:
        return self.blocks[pos.y][pos.x]

def next_paths(vec: Vector, inertia: int) -> list[tuple[Vector, int]]:
    """ Return the possible next paths for this condition """
    # Can't backtrack
    possible = [d for d in DIRECTIONS if d != vec.opposite()]

    inertia += 1
    # Can't exceed inertia of 3
    if inertia > 3:
        possible.remove(vec)

    return [
        (pv, inertia if pv == vec else 0) for pv in possible
    ]


class PathState(NamedTuple):
    cost: int
    inertia: int
    path: tuple[Vector, ...]

PathCostDict: TypeAlias = dict[Position, PathState]

def search(city: City, costs: PathCostDict):

    to_visit = deque()
    origin = Position(0,0)
    costs[origin] = PathState(0, 0, ())

    # Append the only starting path options
    down = PathState(city.block(origin + DOWN), 1, (DOWN,))
    costs[origin + DOWN] = down
    to_visit.append(origin + DOWN)

    right = PathState(city.block(origin + RIGHT), 1, (RIGHT,))
    costs[origin + RIGHT] = right
    to_visit.append(origin + RIGHT)

    while to_visit:
        visiting = to_visit.popleft()
        state = costs[visiting]
        possibles = next_paths(state.path[-1], state.inertia)
        for p in possibles:
            new_vector = p[0]
            new_inertia = p[1]
            new_pos = visiting + new_vector
            if 0 <= new_pos.x < len(city.blocks[0]) and \
               0 <= new_pos.y < len(city.blocks):
                new_cost = state.cost + city.block(new_pos)
                if new_pos in costs and costs[new_pos].cost <= new_cost:
                    pass
                else:
                    new_path = state.path + (new_vector,)
                    costs[new_pos] = PathState(
                        new_cost,
                        new_inertia,
                        new_path,
                    )
                    to_visit.append(new_pos)

    end_of_city = Position(
        len(city.blocks[0]) -1,
        len(city.blocks) -1,
    )
    return costs[end_of_city].cost


def answer_1(lines: Sequence[str]):
    city = City(lines)
    return search(city, PathCostDict())


def answer_2(lines: Sequence[str]):
    pass
