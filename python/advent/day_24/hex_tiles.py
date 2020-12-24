from __future__ import annotations

from itertools import chain

from typing import Dict, List, NewType, Tuple


Coord = NewType("Coord", Tuple[int, int])

BLACK = True
WHITE = False

class Floor:

    def __init__(self):

        self.tiles: Dict[Coord, bool] = {
            Coord((0, 0)): False
        }
        self.current_coord: Coord = Coord((0, 0))

    def __getitem__(self, coord: Coord):
        return self.tiles[coord]

    def move(self, direction: str):

        # 0: 0 1 2 3 4 5 6 7 8
        # 1:  0 1 2 3 4 5 6 7 8
        # 2: 0 1 2 3 4 5 6 7 8
        # 3:  0 1 2 3 4 5 6 7 8
        cx, cy = self.current_coord # current
        dx, dy = 0, 0               # delta
        if len(direction) == 2:
            if direction[0] == "n":
                dy = -1
            else:
                dy = +1

        ny = cy + dy                # new

        dx = 0
        if direction[-1] == "e":
            dx = +1
        else:
            dx = - 1

        nx = cx + dx

        if dy != 0:
            oy = ny % 2                 # oddness
            if oy == 1:
                # Moving to an odd rank
                if dx > 0:
                    nx -=1
            else:
                if dx < 0:
                    nx += 1

        self.current_coord = Coord((nx, ny))

    def flip_tile(self):

        tile = self.tiles.get(self.current_coord, WHITE)
        tile = not tile
        self.tiles[self.current_coord] = tile


    def parse_moves(self, line: str):

        ii = 0
        while ii < len(line):
            c = line[ii]
            if c == "n" or c == "s":
                yield line[ii:ii+2]
                ii += 2
            else:
                yield line[ii]
                ii += 1


    def get_neighbours(self, coord: Coord) -> List[Coord]:
        rv: List[Coord] = []
        cx, cy = coord
        rv.append(Coord((cx + 1, cy)))
        rv.append(Coord((cx - 1, cy)))

        rv.append(Coord((cx, cy + 1)))
        rv.append(Coord((cx, cy - 1)))

        if cy % 2 == 1:
            rv.append(Coord((cx + 1, cy + 1)))
            rv.append(Coord((cx + 1, cy - 1)))
        else:
            rv.append(Coord((cx - 1, cy + 1)))
            rv.append(Coord((cx - 1, cy - 1)))

        return rv


    def lay_tiles(self, lines: List[str]):

        for line in lines:
            self.current_coord = Coord((0, 0))
            for move in self.parse_moves(line):
                self.move(move)
            self.flip_tile()

        return self.count_black()

    def count_black(self):
        return sum(1 for tile in self.tiles.values() if tile)

    def tick(self):

        adjacency: Dict[Coord, int] = {}

        for coord, tile in self.tiles.items():
            if tile == BLACK:
                for neighbour in self.get_neighbours(coord):
                    adjacency[neighbour] = adjacency.get(neighbour, 0) + 1

        new_floor: Dict[Coord, bool] = {} #  self.tiles.copy()
        for coord, count in adjacency.items():
            if count == 2:
                if self.tiles.get(coord, WHITE) == WHITE:
                    new_floor[coord] = BLACK


        for coord, tile in self.tiles.items():
            if tile == BLACK:
                count = adjacency.get(coord, 0)
                if 0 == count or count > 2:
                    new_floor[coord] = WHITE



        self.tiles = new_floor





