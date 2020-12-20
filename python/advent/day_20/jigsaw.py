

from typing import Dict, List, Set


TILE_SIZE = 10


BITS = str.maketrans('.#', '01')

def pixels_int(pixels: str) -> int:
    bits = pixels.translate(BITS)
    return int(bits, 2)


def flipped(value: int, bitsize: int = TILE_SIZE) -> int:
    bits = bin(value)
    flipped_bits = bits[2:].zfill(bitsize)[::-1]
    return int(flipped_bits, 2)


class Tile:

    def __init__(self, lines: List[str]) -> None:
        assert len(lines) == TILE_SIZE + 1
        self.id = int(lines[0].split(' ')[1][:-1])
        self.pixels = lines[1:]

        # borders
        #|-0->
        #|   |
        #3   1
        #|   v
        #v-2->
        self.borders: List[int] = []
        self.borders.append(pixels_int(self.pixels[0]))
        self.borders.append(pixels_int(
            "".join([
                self.pixels[y][9] for y in range(10)
            ])
        ))
        self.borders.append(pixels_int(self.pixels[9]))
        self.borders.append(pixels_int(
            "".join([
                self.pixels[y][0] for y in range(10)
            ])
        ))
        self.flipped_borders = list([
            flipped(border) for border in self.borders
        ])

class Puzzle:

    def __init__(self, lines: List[str]) -> None:

        ii = 0
        self.tiles: Dict[int, Tile] = {}
        while ii < len(lines):
            tile_lines = []
            line = lines[ii]
            while len(line) > 0:
                tile_lines.append(line)
                ii += 1
                line = lines[ii]
            tile = Tile(tile_lines)
            self.tiles[tile.id] = tile
            ii += 1


    def find_edges(self, edginess = 1) -> List[Tile]:

        edges = []
        # Do I have 2 borders that don't match other tiles?
        for index, tile in self.tiles.items():
            unmatched_count = 0
            for border in tile.borders:
                matched = False
                for other_index, other_tile in self.tiles.items():
                    if index == other_index:
                        continue
                    if border in other_tile.borders:
                        matched = True
                        break
                    if border in other_tile.flipped_borders:
                        matched = True
                        break

                if not matched:
                    unmatched_count += 1
            if unmatched_count == edginess:
                edges.append(tile)

        return edges


    def find_corners(self):
        return self.find_edges(edginess = 2)





