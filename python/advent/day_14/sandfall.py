
from typing import List

ORIGIN = (500, 0)

slice = {}


def parse_rocks(lines: List[str]):

    for line in lines:
        coords = [
            (int(c.split(',')[0]), int(c.split(',')[1]))
            for c in line.split(' -> ')
        ]

        for ix in range(1, len(coords)):
            start = coords[ix - 1]
            end = coords[ix]

            sx, sy = start
            ex, ey = end
            dx = ex - sx
            dy = ey - sy
            dx = abs(dx) / dx if dx != 0 else 0
            dy = abs(dy) / dy if dy != 0 else 0

            cx, cy = sx, sy
            current = (cx, cy)

            while current != end:
                cx += dx
                cy += dy









def answer_1(lines: List[str]):
    pass


def answer_2(lines: List[str]):
    pass
