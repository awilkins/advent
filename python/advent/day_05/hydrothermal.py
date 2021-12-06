
from typing import List

class Coord:

    def __init__(self, pair: str):
        self.x, self.y = [ int(c) for c in pair.split(",") ]


class Vector:

    def __init__(self, line):
        self._start, self._end = [ Coord(pair) for pair in line.split(" -> ") ]

    def direction(self, x: int):
        return -1 if x < 0 else 1 if x > 0 else x

    def is_diagonal(self):
        dir_x = self.direction(self._end.x - self._start.x)
        dir_y = self.direction(self._end.y - self._start.y)
        return dir_x != 0 and dir_y != 0

    def points(self):

        dir_x = self.direction(self._end.x - self._start.x)
        dir_y = self.direction(self._end.y - self._start.y)

        x, y = self._start.x, self._start.y

        while x != self._end.x or y != self._end.y:
            yield x, y
            x += dir_x
            y += dir_y

        yield x, y


class SeaBed:

    def __init__(self, lines, size=10):
        self._size = size
        self._vectors = [ Vector(line) for line in lines ]


    def count_overlaps(self, diagonals=False):

        bed_map = [
            [0] * self._size for _ in range(self._size)
        ]

        if diagonals:
            vectors = self._vectors
        else:
            vectors = filter(lambda v: not v.is_diagonal(), self._vectors)

        for vector in vectors:
            for x, y in vector.points():
                bed_map[y][x] += 1

        count = 0
        for y in range(self._size):

            if self._size <= 10:
                print("".join([ str(x) if x > 0 else "." for x in bed_map[y] ]))

            for x in range(self._size):
                if bed_map[y][x] > 1:
                    count += 1

        return count


def answer_1(lines: List[str], size=10):
    seabed = SeaBed(lines, size)
    return seabed.count_overlaps()

def answer_2(lines: List[str], size=10):
    seabed = SeaBed(lines, size)
    return seabed.count_overlaps(diagonals=True)

