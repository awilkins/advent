from __future__ import annotations

from math import sqrt
from itertools import chain, repeat

from typing import Any, Dict, List, Set, Tuple, Union, no_type_check


TILE_SIZE = 10

LEFT = 3
RIGHT = 1
TOP = 0
BOTTOM = 2

VERTICAL = 0
HORIZONTAL = 1

BITS = str.maketrans('.#', '01')

def pixels_int(pixels: str) -> int:
    bits = pixels.translate(BITS)
    return int(bits, 2)

def rotate(original: List[List[Any]]):
    rotated = list(zip(*original[::-1]))
    return list(
        list(t) for t in rotated
    )

def flip_v(original: List[List[Any]]):
    return list(
        row[::-1] for row in original
    )


def flipped(value: int, bitsize: int = TILE_SIZE) -> int:
    bits = bin(value)
    flipped_bits = bits[2:].zfill(bitsize)[::-1]
    return int(flipped_bits, 2)


class Tile:

    def __init__(self, lines: List[str]) -> None:
        assert len(lines) == TILE_SIZE + 1
        self.id = int(lines[0].split(' ')[1][:-1])
        self.pixels = lines[1:]
        self.edges = [False, False, False, False]

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
        self._update_flipped()


    def find_matches(self, others: List[Tile]) -> List[Tuple[int, Tile]]:

        matches = []
        for tile in others:
            if tile is self:
                continue
            for border in self.borders:
                if border in tile.borders or border in tile.flipped_borders:
                    matches.append(
                        (border, tile)
                    )

        return matches


    def __str__(self) -> str:
        return f"Tile {self.id}"

    def _update_flipped(self):
        self.flipped_borders = list([
            flipped(border) for border in self.borders
        ])

    def flip_h(self):
        """ Flip along the horizontal axis (top becomes bottom) """
        self.borders = [
            self.borders[BOTTOM],
            flipped(self.borders[RIGHT]),
            self.borders[TOP],
            flipped(self.borders[LEFT]),
        ]
        self.edges = [
            self.edges[BOTTOM],
            self.edges[RIGHT],
            self.edges[TOP],
            self.edges[LEFT],
        ]
        self._update_flipped()


    def flip_v(self):
        """ Flip alone the vertical axis (left becomes right) """
        self.borders = [
            flipped(self.borders[TOP]),
            self.borders[LEFT],
            flipped(self.borders[BOTTOM]),
            self.borders[RIGHT],
        ]
        self.edges = [
            self.edges[TOP],
            self.edges[LEFT],
            self.edges[BOTTOM],
            self.edges[RIGHT],
        ]
        self._update_flipped()

    def flip_d(self):
        """ Flip along the diagonal axis """
        self.borders = [
            flipped(self.borders[1]),
            flipped(self.borders[0]),
            flipped(self.borders[3]),
            flipped(self.borders[2]),
        ]
        self.edges = [
            self.edges[1],
            self.edges[0],
            self.edges[3],
            self.edges[2],
        ]
        self._update_flipped()


    def rotate(self, count = 1):
        ii = 0
        while ii < count:
            self.borders = [
                self.borders[LEFT],
                self.borders[TOP],
                self.borders[RIGHT],
                self.borders[BOTTOM],
            ]
            self.edges = [
                self.edges[LEFT],
                self.edges[TOP],
                self.edges[RIGHT],
                self.edges[BOTTOM],
            ]
            ii += 1

        self._update_flipped()

    def align(self, alignments: List[Tuple[int, int]]):
        # will always be 1 or 2 values, second one is always TOP

        for position, value in alignments:
            if value not in self.borders:
                axis = self.flipped_borders.index(value) % 2
                if axis == HORIZONTAL:
                    self.flip_h()
                else:
                    self.flip_v()

        rotate_count = 0
        position, value = alignments[0]
        while self.borders[position] != value:
            self.rotate()
            rotate_count += 1
            assert rotate_count < 4

        position, value = alignments[-1]
        if self.borders[position] != value:
            # Reverse the tile order
            self.flip_h()
            self.flip_v()
            self.flip_d()

        while self.borders[position] != value:
            self.rotate()



class NullTile(Tile):

    def __init__(self) -> None:
        self.id = -1

EMPTY = NullTile()

class Puzzle:

    def __init__(self, lines: List[str]) -> None:

        ii = 0
        self.tiles: Dict[int, Tile] = {}
        self.borders: Dict[int, List[Tile]] = {}
        while ii < len(lines):
            tile_lines = []
            line = lines[ii]
            while len(line) > 0:
                tile_lines.append(line)
                ii += 1
                line = lines[ii]
            tile = Tile(tile_lines)
            self.tiles[tile.id] = tile
            for border in tile.borders:
                tiles = self.borders[border] = self.borders.get(border, [])
                tiles.append(tile)
                # All border IDs are pairs only
                assert len(tiles) < 3
            for border in tile.flipped_borders:
                tiles = self.borders[border] = self.borders.get(border, [])
                tiles.append(tile)
                # All border IDs are pairs only
                assert len(tiles) < 3

            ii += 1
        corners = self.find_corners()
        self.matrix = self.solve_matrix(corners[0])


    def find_edges(self, edginess = 1) -> List[Tile]:

        edges = []
        # Do I have borders that don't match other tiles?
        for index, tile in self.tiles.items():
            unmatched_count = 0
            for border_index, border in enumerate(tile.borders):
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
                    tile.edges[border_index] = True
                    unmatched_count += 1

            if unmatched_count == edginess:
                edges.append(tile)

        return edges


    def find_corners(self):
        return self.find_edges(edginess = 2)



    def count_empty_squares(self, matrix: List[List[Tile]]) -> int:
        count = 0
        for row in matrix:
            if -1 in [tile.id for tile in row]:
                count += 1

        return count


    def solve_matrix(self, start: Tile):

        puzzle_size = int(sqrt(len(self.tiles)))

        matrix: List[List[Tile]] = []
        for _ in range(puzzle_size):
            matrix.append(
                list(repeat(EMPTY, puzzle_size))
            )

        while not (start.edges[LEFT] and start.edges[TOP]):
            start.rotate()

        matrix[0][0] = start
        used_tiles = [start]

        for yy in range(puzzle_size):
            for xx in range(puzzle_size):
                tile = matrix[yy][xx]
                if tile is not EMPTY:
                    continue

                alignments: List[Tuple[int, int]] =[]

                if xx == 0:
                    last_tile = matrix[yy - 1][xx]
                    last_border = last_tile.borders[BOTTOM]
                    alignments.append((TOP, last_border))
                else:
                    last_tile = matrix[yy][xx - 1]
                    last_border = last_tile.borders[RIGHT]
                    alignments.append((LEFT, last_border))
                    if yy > 0:
                        upper_tile = matrix[yy - 1][xx]
                        alignments.append((TOP, upper_tile.borders[BOTTOM]))

                matches = list(t for t in self.borders[last_border] if t is not last_tile)

                assert len(matches) == 1
                next_tile = matches[0]
                assert next_tile not in used_tiles
                used_tiles.append(next_tile)
                print(f'Used tile : {next_tile.id}')

                next_tile.align(alignments)

                # fixup edges
                if yy == 0:
                    if not next_tile.edges[TOP]:
                        next_tile.rotate(2)
                        next_tile.flip_v()
                    assert next_tile.edges[TOP]

                if xx == 0:
                    if not next_tile.edges[LEFT]:
                        next_tile.rotate(2)
                        next_tile.flip_h()
                    assert next_tile.edges[LEFT]

                matrix[yy][xx] = next_tile

        for yy in range(1, puzzle_size - 1):
            for xx in range(1, puzzle_size - 1):
                tile = matrix[yy][xx]
                assert tile.borders[TOP] == matrix[yy - 1][xx].borders[BOTTOM]
                assert tile.borders[BOTTOM] == matrix[yy + 1][xx].borders[TOP]
                assert tile.borders[LEFT] == matrix[yy][xx - 1].borders[RIGHT]
                assert tile.borders[RIGHT] == matrix[yy][xx + 1].borders[LEFT]

        return matrix





