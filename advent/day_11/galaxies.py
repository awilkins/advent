from __future__ import annotations

from itertools import combinations

from typing import Sequence, List, NamedTuple

class Position(NamedTuple):
    x: int
    y: int
    
    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

class Universe:
    

    height: int
    width: int
    galaxies: List[Position]
    
    def __init__(self, lines: Sequence[str]):
        self.galaxies = []
        self.width = len(lines[0])
        self.height = len(lines)
        for yy, line in enumerate(lines):
            for xx, char in enumerate(line):
                if char == '#':
                    self.galaxies.append(
                        Position(xx, yy)
                    )
        # Expand space
    
    def expand(self, factor = 2):
        yy = 0
        factor = factor - 1
        while yy < self.height:
            if not any(galaxy for galaxy in self.galaxies if galaxy.y == yy):
                self.height += factor
                for index, galaxy in enumerate(self.galaxies):
                     if galaxy.y > yy:
                        self.galaxies[index] = Position(
                            galaxy.x, galaxy.y + factor
                        )
                yy += factor
            yy += 1
        # Expand space
        xx = 0
        while xx < self.width:
            if not any(galaxy for galaxy in self.galaxies if galaxy.x == xx):
                self.width += factor
                for index, galaxy in enumerate(self.galaxies):
                    if galaxy.x > xx:
                        self.galaxies[index] = Position(
                            galaxy.x + factor, galaxy.y 
                        )
                xx += factor            
            xx += 1            

def answer_1(lines: Sequence[str]):
    universe = Universe(lines)
    universe.expand()
    pairs = combinations(universe.galaxies, 2)

    return sum(one.distance(two) for one, two in pairs)
    


def answer_2(lines: Sequence[str], factor):
    universe = Universe(lines)
    universe.expand(factor)
    pairs = combinations(universe.galaxies, 2)

    return sum(one.distance(two) for one, two in pairs)
