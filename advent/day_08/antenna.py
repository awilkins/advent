from __future__ import annotations

from typing import Sequence

from itertools import permutations, chain
from math import gcd

Coord = tuple[int, int]


def generate_antinode(one, two):
    x2, y2 = two
    x1, y1 = one

    xn = x1 + (x1 - x2)
    yn = y1 + (y1 - y2)
    return (xn, yn)


def generate_harmonic_antinodes(one, two, max_x, max_y):
    x1, y1 = one
    x2, y2 = two

    # raw vector
    vx = x1 - x2
    vy = y1 - y2

    # ANY distance so 4, 4 is really a vector of 1, 1
    d = gcd(vx, vy)
    vx //= d
    vy //= d

    xx, yy = two
    xx += vx
    yy += vy
    while (0 <= xx < max_x) and (0 <= yy < max_y):
        yield (xx, yy)
        xx += vx
        yy += vy


class Map:
    rows: list[str]
    antennae: dict[str, list[Coord]]

    def __init__(self, lines: Sequence[str]):
        self.rows = list(lines)
        self.antennae = dict()

        for yy, row in enumerate(lines):
            for xx, cell in enumerate(row):
                if cell.isalpha() or cell.isdigit():
                    antenna_pool = self.antennae.setdefault(cell, list())
                    antenna_pool.append((xx, yy))

    def get_square(self, coord: Coord):
        xx, yy = coord
        return self.rows[yy][xx]

    def get_antenna_freq(self):
        return self.antennae.keys()

    def get_antinodes(self, frequency):
        antenna_freq = self.antennae.get(frequency)
        assert antenna_freq is not None
        antinodes = set(
            generate_antinode(one, two) for one, two in permutations(antenna_freq, r=2)
        )
        return {
            (xx, yy)
            for xx, yy in antinodes
            if 0 <= xx < len(self.rows[0]) and 0 <= yy < len(self.rows)
        }

    def get_all_antinodes(self):
        return set.union(*(self.get_antinodes(f) for f in self.get_antenna_freq()))

    def get_harmonic_antinodes(self, freq) -> set[Coord]:
        antennas_freq = self.antennae.get(freq)
        assert antennas_freq is not None
        generators = [
            generate_harmonic_antinodes(one, two, len(self.rows[0]), len(self.rows))
            for one, two in permutations(antennas_freq, r=2)
        ]
        antinodes = set()
        for gen in generators:
            nodeline: set[Coord] = set(gen)
            antinodes = antinodes.union(nodeline)
        return antinodes

    def get_all_harmomic_antinodes(self) -> set[Coord]:
        return set.union(
            *(self.get_harmonic_antinodes(f) for f in self.get_antenna_freq())
        )


def answer_1(lines: Sequence[str]):
    map = Map(lines)
    return len(map.get_all_antinodes())


def answer_2(lines: Sequence[str]):
    map = Map(lines)
    return len(map.get_all_harmomic_antinodes())
