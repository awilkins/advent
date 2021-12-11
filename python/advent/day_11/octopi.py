
from itertools import product
from typing import List, Tuple

def surrounds(m, x, y):
    """Stolen from day 9"""
    return [
        (sx, sy) for sx, sy in product(
            range(x - 1, x + 2),
            range(y - 1, y + 2)
        )
        if
            sx >= 0 and sx < len(m[0]) and
            sy >= 0 and sy < len(m) and
            not (sx == x and sy == y)
    ]


def make_map(lines: List[str]) -> List[List[int]]:
    return [
        [
            int(d) for d in l
        ] for l in lines
    ]


def increment_map(m: List[List[int]]) -> List[List[int]]:
    for y, row in enumerate(m):
        for x, col in enumerate(row):
            m[y][x] = col + 1

    return m


def flash_map(m: List[List[int]]) -> Tuple[List[List[int]], int]:

    triggered = [ (fx, fy) for fx, fy in product(
        range(len(m[0])),
        range(len(m)),
    ) if m[fy][fx] == 10]

    while len(triggered):
        flashers = triggered
        triggered = []
        for fx, fy in flashers:
            for tx, ty in surrounds(m, fx, fy):
                m[ty][tx] += 1
                if m[ty][tx] == 10:
                    triggered.append((tx, ty))

    flashed = [ (fx, fy) for fx, fy in product(
        range(len(m[0])),
        range(len(m)),
    ) if m[fy][fx] > 9]

    for fx, fy in flashed:
        m[fy][fx] = 0

    return m, len(flashed)


def cycle_map(m, count) -> int:

    total_flashes = 0
    for c in range(count):
        increment_map(m)
        m, flashes = flash_map(m)
        total_flashes += flashes

    return total_flashes


def first_flash(m) -> int:

    step_count = 0
    map_size = sum([ len(row) for row in m ])
    while True:
        increment_map(m)
        m, flashes = flash_map(m)
        step_count += 1
        if flashes == map_size:
            return step_count


