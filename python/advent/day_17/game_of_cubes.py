from __future__ import annotations

from typing import Dict, List, NewType, Set, Tuple


Coord = NewType('Coord', Tuple[int, int, int, int])

class Cube:

    def __init__(self, coord: Coord, dimensions: int = 3) -> None:
        self.coord = coord
        self.dimensions = dimensions


    def neighbours(self) -> List[Coord]:

        n: List[Coord] = []
        x, y, z, w = self.coord

        w_range = [0]
        if self.dimensions == 4:
            w_range = range(w - 1, w + 2)

        for ww in w_range:
            for zz in range(z - 1, z + 2):
                for yy in range(y - 1, y + 2):
                    for xx in range(x - 1, x + 2):
                        c = Coord((xx, yy, zz, ww))
                        if c != self.coord:
                            n.append(Coord((xx, yy, zz, ww)))

        return n


class CubeSpace:

    def __init__(self, plane: List[Coord], dimensions:int = 3) -> None:
        self.space: Set[Coord] = set(plane)
        self.dimensions = dimensions

    def count(self) -> int:
        return len(self.space)

    def cycle(self) -> CubeSpace:
        activity: Dict[Coord, int] = {}

        current_space: Set[Coord] = self.space
        next_space: Set[Coord] = set()

        for cube in [Cube(coord, self.dimensions) for coord in current_space]:
            for coord in cube.neighbours():
                activity[coord] = activity.get(coord, 0) + 1

        for coord, count in activity.items():

            if count == 3 or (count == 2 and coord in current_space):
                next_space.add(coord)

        return CubeSpace(list(next_space), self.dimensions)


    def __str__(self) -> str:
        low_x = min([x for x, _, _, _ in self.space])
        low_y = min([y for _, y, _, _ in self.space])
        low_z = min([z for _, _, z, _ in self.space])
        low_w = min([w for _, _, _, w in self.space])
        high_x = max([x for x, _, _, _ in self.space])
        high_y = max([y for _, y, _, _ in self.space])
        high_z = max([z for _, _, z, _ in self.space])
        high_w = max([w for _, _, _, w in self.space])

        metaplanes = []
        for ww in range(low_w, high_w + 1):
            planes = []
            for zz in range(low_z, high_z + 1):

                if self.dimensions == 3:
                    planes.append(f'\nz={zz}\n')
                if self.dimensions == 4:
                    planes.append(f'\nz={zz}, w={ww}\n')

                rows = []
                for yy in range(low_y, high_y + 1):
                    row = []
                    for xx in range(low_x, high_x + 1):
                        if (xx, yy, zz, ww) in self.space:
                            row.append('#')
                        else:
                            row.append('.')
                    row.append('\n')
                    rows.append("".join(row))
                planes.append("".join(rows))
            metaplanes.append("".join(planes))

        return "".join(metaplanes)


def parse_plane(plane: List[str]) -> List[Coord]:

    p: List[Coord] = []
    for yy, row in enumerate(plane):
        for xx, col in enumerate(row):
            if col == "#":
                p.append(Coord((xx, yy, 0, 0)))

    return p
