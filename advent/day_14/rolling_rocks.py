from __future__ import annotations

from typing import Sequence, List

class World:

    field: List[List[str]]
    
    def __init__(self, lines: Sequence[str]):
        self.field = [
            [c for c in line]
            for line in lines
        ]

    def __str__(self):
        return "\n".join(
            "".join(line) for line in self.field
        )

    def roll_north(self):
        previous = [
            line.copy() for line in self.field
        ]
        for yindex, line in enumerate(self.field[1:]):
            for xindex, c in enumerate(line):
                if c == 'O' and self.field[yindex][xindex] == '.':
                    line[xindex] = '.'
                    self.field[yindex][xindex] = 'O'
        return self.field != previous

    def full_roll_north(self):
        while self.roll_north():
            pass
    
    def roll_west(self):
        previous = [
            line.copy() for line in self.field
        ]
        for line in self.field:
            for xindex in range(1, len(line)):
                c = line[xindex]
                if c == 'O' and line[xindex - 1] == '.': 
                    line[xindex] = '.'
                    line[xindex - 1] = 'O'
        return self.field != previous

    def full_roll_west(self):
        while self.roll_west():
            pass
    
    def roll_south(self):
        previous = [
            line.copy() for line in self.field
        ]
        for yindex in range(len(self.field) -2, -1, -1):
            line = self.field[yindex]
            for xindex, c in enumerate(line):
                if c == 'O' and self.field[yindex + 1][xindex] == '.':
                    line[xindex] = '.'
                    self.field[yindex + 1][xindex] = 'O'
        return self.field != previous

    def full_roll_south(self):
        while self.roll_south():
            pass
    
    def roll_east(self):
        previous = [
            line.copy() for line in self.field
        ]
        for line in self.field:
            for xindex in range(len(line) -2, -1, -1):
                c = line[xindex]
                if c == 'O' and line[xindex + 1] == '.':
                    line[xindex] = '.'
                    line[xindex + 1] = 'O'
        return self.field != previous

    def full_roll_east(self):
        while self.roll_east():
            pass
    
    def cycle(self):
        self.full_roll_north()
        self.full_roll_west()
        self.full_roll_south()
        self.full_roll_east()

    def load(self) -> int:
        
        load = 0
        for yindex, line in enumerate(self.field):
            load_factor = len(self.field) - yindex
            for c in line:
                if c == 'O':
                    load += load_factor
        
        return load
                

def answer_1(lines: Sequence[str]):
    world = World(lines)
    world.full_roll_north()
    return world.load()


def answer_2(lines: Sequence[str]):
    world = World(lines)
    worlds = {}
    index = 0
    for index in range(1_000_000_000):
        world.cycle()
        sworld = str(world)
        if sworld in worlds:
            cycle_length = index - worlds[sworld] 
            target = (1_000_000_000 - (index + 1)) % cycle_length
            for i in range(target):
                world.cycle()
            return world.load()
        worlds[sworld] = index
        
    
    print()
    print(index)
    print(world)
    return world.load()
