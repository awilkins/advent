from __future__ import annotations

from math import sqrt
from itertools import chain, repeat

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
        self.flipped_borders = list([
            flipped(border) for border in self.borders
        ])


    def find_matches(self, others: List[Tile]) -> List[Tile]:

        matches = []
        for tile in others:
            if tile is self:
                continue
            for border in self.borders:
                if border in tile.borders or border in tile.flipped_borders:
                    matches.append(tile)

        return matches

    def __str__(self) -> str:
        return f"Tile {self.id}"


class NullTile(Tile):

    def __init__(self) -> None:
        self.id = -1

EMPTY = NullTile()
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


    def solve_edge(self, start: Tile, remaining_edges: List[Tile], remaining_corners: List[Tile]) -> List[Tile]:

        top_row: List[Tile] = []
        # Arbitrary pick for top corner
        top_row.append(start)
        remaining_corners.remove(top_row[0])

        matches = top_row[0].find_matches(remaining_edges)

        # Filter matches : matched edge must be next to unused edge
        top_row.append(matches[0])

        remaining_edges.remove(top_row[1])

        puzzle_size = int(sqrt(len(self.tiles)))
        edge_size = puzzle_size - 2
        xx = 1
        while xx < edge_size:
            matches = top_row[1].find_matches(remaining_edges)
            assert len(matches) == 1
            top_row.append(matches[0])
            xx += 1

        # Finally the corner
        matches = top_row[-1].find_matches(remaining_corners)

        assert len(matches) == 1
        top_row.append(matches[0])

        return top_row

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
        for _ in range(3):
            edge = self.solve_edge(
                next_corner,
                edges,
                corners,
            )
            solved_edges.append(edge)
            next_corner = edge[-1]
        # last edge
        corners.append(first_corner)
        solved_edges.append(self.solve_edge(
            next_corner,
            edges,
            corners,
        ))

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


    def solve_matrix(self, edges: List[List[Tile]], matrix: List[List[Tile]]):

        puzzle_size = int(sqrt(len(self.tiles)))
        remaining_tiles = list(self.tiles.values())
        for edge in edges:
            for tile in edge:
                if tile in remaining_tiles:
                    remaining_tiles.remove(tile)


        last_count = self.count_empty_squares(matrix)
        while last_count > 0:
            for yy in range(1, puzzle_size - 1):
                for xx in range(1, puzzle_size - 1):

                    tile: Tile = matrix[yy][xx]
                    if tile is not EMPTY:
                        continue

                    neighbours = [
                        matrix[yy    ][xx - 1], # To the left ...
                        matrix[yy    ][xx + 1], # To the right ...
                        matrix[yy + 1][xx    ], # Underneath ...
                        matrix[yy - 1][xx    ], # Up above ...
                    ] # Outta sight....

                    neighbours = [
                        ntile for ntile in neighbours
                        if not ntile is tile and not ntile is EMPTY
                    ]

                    potential_tiles = []
                    for rtile in remaining_tiles:
                        matches = rtile.find_matches(neighbours)

                        if len(matches) == len(neighbours):
                            potential_tiles.append(rtile)

                    if len(potential_tiles) == 1:
                        found_tile = potential_tiles[0]
                        matrix[yy][xx] = found_tile
                        remaining_tiles.remove(found_tile)

            new_count = self.count_empty_squares(matrix)
            if new_count == last_count:
                raise RuntimeError("No progress!")
            last_count = new_count

    def solve(self):

        edges = self.solve_edges()
        matrix = self.get_matrix(edges)
        self.solve_matrix(edges, matrix)

        assert self.count_empty_squares(matrix) == 0




















