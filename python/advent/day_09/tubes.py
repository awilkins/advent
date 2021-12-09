
from itertools import product

from typing import List, Tuple


def is_low(map: List[List[int]], x, y) -> bool:

    for map_y in range(
        max(0, y - 1),
        min(len(map), y + 2)
    ):
        for map_x in range(
            max(0, x - 1),
            min(len(map[0]), x + 2)
        ):

            if map_x == x and map_y == y:
                continue
            if map[y][x] >= map[map_y][map_x]:
                return False

    return True


def make_map(lines: List[str]) -> List[List[int]]:
    return [
        [
            int(d) for d in l
        ] for l in lines
    ]


def map_risk(map) -> int:
    return sum(
        [
            map[y][x] + 1 for x, y in product(range(len(map[0])), range(len(map)))
            if is_low(map, x, y)
        ]
    )





def answer_1(lines: List[str]) -> int:
    map = make_map(lines)
    return map_risk(map)
