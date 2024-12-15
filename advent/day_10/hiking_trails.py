from __future__ import annotations

from typing import Sequence, List

from collections import deque


class Map:
    squares: list[list[int]]

    def __init__(self, lines) -> None:
        self.squares = [[int(n) for n in line] for line in lines]

    def height(self, coord) -> int:
        x, y = coord
        return self.squares[y][x]

    def in_bounds(self, coord) -> int:
        x, y = coord
        return 0 <= x < len(self.squares[0]) and 0 <= y < len(self.squares)

    def trailheads(self) -> set[Coord]:
        heads = set()
        for y in range(len(self.squares)):
            for x in range(len(self.squares[0])):
                coord = (x, y)
                if self.height(coord) == 0:
                    heads.add(coord)
        return heads


Coord = tuple[int, int]


class Hiker:
    map: Map

    visited: set[Coord]
    to_visit: deque

    current_location: Coord
    route_score: int

    def __init__(self, map: Map) -> None:
        self.map = map
        self.visited = set()
        self.to_visit = deque()
        self.route_score = 0

    def next_nodes(self) -> set[Coord]:
        x, y = self.current_location
        return set(
            node
            for node in [
                (x - 1, y),
                (x + 1, y),
                (x, y - 1),
                (x, y + 1),
            ]
            if self.map.in_bounds(node)
            and self.map.height(node) == self.map.height(self.current_location) + 1
        )

    def hike(self):
        self.visited.add(self.current_location)
        if self.map.height(self.current_location) == 9:
            self.route_score += 1
        self.to_visit.extend(self.next_nodes())
        if len(self.to_visit):
            self.current_location = self.to_visit.popleft()
            self.hike()

    def score(self):
        return sum(1 for node in self.visited if self.map.height(node) == 9)


def answer_1(lines: Sequence[str]):
    map = Map(lines)
    trails = map.trailheads()
    total = 0
    for trail in trails:
        hiker = Hiker(map)
        hiker.current_location = trail
        hiker.hike()
        total += hiker.score()
    return total


def answer_2(lines: Sequence[str]):
    map = Map(lines)
    trails = map.trailheads()
    total = 0
    for trail in trails:
        hiker = Hiker(map)
        hiker.current_location = trail
        hiker.hike()
        total += hiker.route_score
    return total
