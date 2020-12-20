from __future__ import annotations

from math import sqrt
from itertools import chain, repeat

from typing import Any, Dict, List, Set, Tuple, no_type_check


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

    def align(self, value, border=LEFT):
        if value not in self.borders:
            axis = self.flipped_borders.index(value) % 2
            if axis == VERTICAL:
                self.flip_v()
            else:
                self.flip_h()

        while self.borders[border] != value:
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


    def solve_edge(self, start: Tile) -> List[Tile]:
        # Check it's really a corner
        assert sum(start.edges) == 2
        puzzle_size = sqrt(len(self.tiles))
        row: List[Tile] = []
        row.append(start)
        # rotate corner so that it's top left
        while not (start.edges[TOP] and start.edges[LEFT]):
            start.rotate()

        last_tile = start
        xx = 1
        while xx < puzzle_size:
            next_tiles = [tile for tile in self.borders[last_tile.borders[RIGHT]] if tile is not last_tile]
            assert len(next_tiles) == 1
            next_tile = next_tiles[0]
            row.append(next_tile)
            next_tile.align(last_tile.borders[RIGHT])
            last_tile = next_tile
            xx += 1

        # Check end is a corner
        assert sum(row[-1].edges) == 2

        return row

    def solve_edges(self):

        # First, find the corners and edges
        corners = self.find_corners()
        assert len(corners) == 4
        edges = self.find_edges()
        puzzle_size = sqrt(len(self.tiles))
        edge_size = puzzle_size - 2
        assert len(edges) == edge_size * 4

        first_corner = corners[0]
        solved_edges: List[List[Tile]] = []

        next_corner = first_corner
        while len(solved_edges) < 4:
            solved_edges.append(
                self.solve_edge(next_corner)
            )
            next_corner = solved_edges[-1][-1]
            next_corner.rotate(LEFT)

        return solved_edges

    def get_matrix(self, edges):
        puzzle_size = int(sqrt(len(self.tiles)))

        top, right, bottom, left = edges

        rows = []
        rows.append(top)
        yy = 1
        while yy < puzzle_size - 1:
            new_row = [ left[-(yy+1)] ]
            new_row.extend(repeat(EMPTY, puzzle_size - 2))
            new_row.append(right[yy])
            rows.append(new_row)
            yy += 1
        rows.append(bottom[::-1])
        return rows


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

        for yy in range(puzzle_size):
            for xx in range(puzzle_size):
                tile = matrix[yy][xx]
                if tile is not EMPTY:
                    continue

                if xx == 0:
                    last_tile = matrix[yy - 1][xx]
                    last_border = last_tile.borders[BOTTOM]
                    alignment_border = TOP
                else:
                    last_tile = matrix[yy][xx - 1]
                    last_border = last_tile.borders[RIGHT]
                    alignment_border = LEFT

                matches = list(t for t in self.borders[last_border] if t is not last_tile)
                assert len(matches) == 1
                next_tile = matches[0]
                next_tile.align(last_border, alignment_border)

                # check edges
                if yy == 0:
                    if not next_tile.edges[TOP]:
                        next_tile.rotate(2)
                        next_tile.flip_v()
                    assert next_tile.edges[TOP]
                elif yy == puzzle_size - 1:
                    if not next_tile.edges[BOTTOM]:
                        next_tile.rotate(2)
                        next_tile.flip_v()
                    assert next_tile.edges[BOTTOM]
                else:
                    upper_tile = matrix[yy - 1][xx]
                    if upper_tile.borders[BOTTOM] != next_tile.borders[TOP]:
                        next_tile.rotate(2)
                        next_tile.flip_v()
                    assert upper_tile.borders[BOTTOM] == next_tile.borders[TOP]


                if xx == 0:
                    if not next_tile.edges[LEFT]:
                        next_tile.rotate(2)
                        next_tile.flip_h()
                    assert next_tile.edges[LEFT]
                if xx == puzzle_size -1:
                    if not next_tile.edges[RIGHT]:
                        next_tile.rotate(2)
                        next_tile.flip_h()
                    assert next_tile.edges[RIGHT]

                matrix[yy][xx] = next_tile

        for yy in range(1, puzzle_size - 1):
            for xx in range(1, puzzle_size - 1):
                tile = matrix[yy][xx]
                assert tile.borders[TOP] == matrix[yy - 1][xx].borders[BOTTOM]
                assert tile.borders[BOTTOM] == matrix[yy + 1][xx].borders[TOP]
                assert tile.borders[LEFT] == matrix[yy][xx - 1].borders[RIGHT]
                assert tile.borders[RIGHT] == matrix[yy][xx + 1].borders[LEFT]

        return matrix





