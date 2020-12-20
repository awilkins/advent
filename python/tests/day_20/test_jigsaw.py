from math import exp
from unittest import TestCase

from ..util import get_resource

DAY="20"

from advent.day_20.jigsaw import *

TILE_2311 = """\
Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###
"""

class TestPuzzle(TestCase):

    def test_bitflip(self):

        expected = int('1000000000', 2)
        actual = flipped(1)
        self.assertEqual(expected, actual)


    def test_pixels_int(self):
        expected = 1
        actual = pixels_int('.........#')

        self.assertEqual(expected, actual)


    def test_tile(self):

        tile = Tile(TILE_2311.splitlines())

        self.assertEqual(2311, tile.id)
        self.assertListEqual([
            210,
            89,
            231,
            498,
        ], tile.borders)


    def test_puzzle(self):
        lines = get_resource(f'day_{DAY}/example_1.txt').read_text().splitlines()
        puzzle = Puzzle(lines)

        self.assertEqual(9, len(puzzle.tiles))

        self.assertListEqual([
            2311, 1951, 1171, 1427, 1489, 2473, 2971, 2729, 3079
        ], list(puzzle.tiles.keys()))

    def test_example_1(self):
        lines = get_resource(f'day_{DAY}/example_1.txt').read_text().splitlines()
        puzzle = Puzzle(lines)

        corners = puzzle.find_corners()
        self.assertEqual(4, len(corners))
        product = 1
        for tile in corners:
            product *= tile.id

        self.assertEqual(20899048083289, product)


    def test_find_edges(self):
        lines = get_resource(f'day_{DAY}/example_1.txt').read_text().splitlines()
        puzzle = Puzzle(lines)

        edges = puzzle.find_edges()
        self.assertEqual(4, len(edges))

        # Main puzzle is 144 tiles, 12 square, so 40 edges
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
        puzzle = Puzzle(lines)

        corners = puzzle.find_corners()
        self.assertEqual(4, len(corners))
        edges = puzzle.find_edges()
        self.assertEqual(40, len(edges))

    def test_answer_1(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
        puzzle = Puzzle(lines)

        corners = puzzle.find_corners()
        self.assertEqual(4, len(corners))
        product = 1

        for tile in corners:
            product *= tile.id

        answer = product
        print(f'\nAnswer 1 : {answer}\n')

        expected = 7901522557967
        self.assertEqual(expected, answer)


    def test_solve_edges(self):
        lines = get_resource(f'day_{DAY}/example_1.txt').read_text().splitlines()
        puzzle = Puzzle(lines)

        row = puzzle.solve_edge(puzzle.tiles[1951], puzzle.find_edges(), puzzle.find_corners())
        expected = [ 1951, 2311, 3079 ]
        actual = list(tile.id for tile in row)
        self.assertListEqual(expected, actual)

        edges = puzzle.solve_edges()
        expected = [
            [1951, 2311, 3079],
            [3079, 2473, 1171],
            [1171, 1489, 2971],
            [2971, 2729, 1951],
        ]
        edge_ids = list([
           t.id for t in edge
        ] for edge in edges)
        self.assertListEqual(expected, edge_ids)


    def test_matrix(self):
        lines = get_resource(f'day_{DAY}/example_1.txt').read_text().splitlines()
        puzzle = Puzzle(lines)
        edges = puzzle.solve_edges()

        expected = [
            [1951, 2311, 3079],
            [2729, -1  , 2473],
            [2971, 1489, 1171],
        ]
        matrix = puzzle.get_matrix(edges)
        matrix_ids = list([
            t.id for t in matrix_row
        ] for matrix_row in matrix)
        self.assertListEqual(expected, matrix_ids)

        puzzle.solve_matrix(edges, matrix)
        expected[1][1] = 1427
        matrix_ids = list([
            t.id for t in matrix_row
        ] for matrix_row in matrix)
        self.assertListEqual(expected, matrix_ids)


    def test_answer_2(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
        puzzle = Puzzle(lines)

        puzzle.solve()

        # answer =
        # print(f'\nAnswer 2 : {answer}\n')

        # expected =
        # self.assertEqual(expected, answer)

