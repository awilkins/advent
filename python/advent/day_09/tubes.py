
from itertools import product

from typing import List, Tuple


def surrounds(map, x, y):
    return [
        (sx, sy) for sx, sy in [
            (x - 1, y),
            (x, y - 1),
            (x + 1, y),
            (x, y + 1),
        ]
        if
            sx >= 0 and sx < len(map[0]) and
            sy >= 0 and sy < len(map) and
            not (sx == x and sy == y)
    ]


def is_low(map: List[List[int]], x, y) -> bool:

    for map_x, map_y in surrounds(map, x, y):
        if map[y][x] >= map[map_y][map_x]:
            return False

    return True


def make_map(lines: List[str]) -> List[List[int]]:
    return [
        [
            int(d) for d in l
        ] for l in lines
    ]


def lowpoints(map) -> List[Tuple[int, int]]:
    return [
            (x, y) for x, y in product(range(len(map[0])), range(len(map)))
            if is_low(map, x, y)
        ]


def map_risk(map) -> int:
    return sum(
        map[y][x] + 1 for x, y in lowpoints(map)
    )


def basin(map, x, y):

    def spread(x: int, y: int) -> List[Tuple[int, int]]:
        return [
            (bx, by) for bx, by in surrounds(map, x, y)
            if map[by][bx] < 9
        ]

    s = spread(x, y)
    b = set(s)
    b.add((x, y))

    current_size = len(b)
    while True:

        next_spread = set()
        for x, y in s:
            next_spread.update([
                (sx, sy) for sx, sy in spread(x, y)
                if (sx, sy) not in b
            ])

        b.update(next_spread)
        s = next_spread

        if len(b) == current_size:
            break
        current_size = len(b)

    return b


def answer_1(lines: List[str]) -> int:
    m = make_map(lines)
    return map_risk(m)


def answer_2(lines: List[str]) -> int:
    m = make_map(lines)
    basins = [
        basin(m, x, y) for x, y in lowpoints(m)
    ]
    basins = sorted(
        basins,
        key=lambda b : len(b),
        reverse=True
    )
    return len(basins[0]) * len(basins[1]) * len(basins[2])
