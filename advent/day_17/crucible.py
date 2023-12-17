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
    if inertia > 2:
        possible.remove(vec)

    return [
        (pv, inertia if pv == vec else 0) for pv in possible
    ]

def ultra_paths(vec: Vector, inertia: int) -> list[tuple[Vector, int]]:
    """ Return the possible next paths for this condition """
    inertia += 1
    # Can't change direction without inertia 4
    if inertia < 4:
        return [(vec, inertia)]

    # Can't backtrack
    possible = [d for d in DIRECTIONS if d != vec.opposite()]

    if inertia > 9:
        possible.remove(vec)

    return [
        (pv, inertia if pv == vec else 0) for pv in possible
    ]

class PathState(NamedTuple):
    cost: int
    inertia: int
    path: tuple[Vector, ...]

class StateKey(NamedTuple):
    position: Position
    vector: Vector
    inertia: int

PathCostDict: TypeAlias = dict[StateKey, PathState]

def search(city: City, costs: PathCostDict, crucible_func=next_paths):

    to_visit: deque[StateKey] = deque()
    origin = Position(0,0)

    # Append the only starting path options
    down = PathState(city.block(origin + DOWN), 0, (DOWN,))
    state_key = StateKey(origin + DOWN, DOWN, 0)
    costs[state_key] = down
    to_visit.append(state_key)

    right = PathState(city.block(origin + RIGHT), 0, (RIGHT,))
    state_key = StateKey(origin + RIGHT, RIGHT, 0)
    costs[state_key] = right
    to_visit.append(state_key)

    while to_visit:
        visiting = to_visit.popleft()
        state = costs[visiting]
        possibles = crucible_func(state.path[-1], state.inertia)
        for p in possibles:
            new_vector = p[0]
            new_inertia = p[1]
            new_pos = visiting.position + new_vector
            if 0 <= new_pos.x < len(city.blocks[0]) and \
               0 <= new_pos.y < len(city.blocks):
                new_cost = state.cost + city.block(new_pos)
                new_key = StateKey(new_pos, new_vector, new_inertia)
                if new_key in costs and costs[new_key].cost <= new_cost:
                    pass
                else:
                    new_path = state.path + (new_vector,)
                    costs[new_key] = PathState(
                        new_cost,
                        new_inertia,
                        new_path,
                    )
                    to_visit.append(new_key)

    end_of_city = Position(
        len(city.blocks[0]) -1,
        len(city.blocks) -1,
    )
    end_keys = [key for key in costs.keys() if key.position == end_of_city]
    return min(state.cost for state in [costs[key] for key in end_keys])


def answer_1(lines: Sequence[str]):
    city = City(lines)
    return search(city, PathCostDict())


def answer_2(lines: Sequence[str]):
    city = City(lines)
    return search(city, PathCostDict(), ultra_paths)
