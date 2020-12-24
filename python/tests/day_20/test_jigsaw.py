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
        actual = pixels_int(list('.........#'))

        self.assertEqual(expected, actual)


    def test_flip_d(self):

        original = [
            list(s) for s in [
                "ABC",
                "DEF",
                "GHI",
            ]
        ]
        expected = [
            list(s) for s in [
                "IFC",
                "HEB",
                "GDA",
            ]
        ]
        actual = flip_d(original)
        self.assertListEqual(expected, actual)


    def test_tile(self):

        tile = Tile(TILE_2311.splitlines())

        self.assertEqual(2311, tile.id)
        self.assertListEqual([
            210,
            89,
            231,
            498,
        ], tile.borders)

    def test_tile_flip_h(self):
        tile = Tile(TILE_2311.splitlines())

        borders = tile.borders.copy()
        flipped_borders = tile.flipped_borders.copy()

        tile.flip_h()
        assert tile.borders[TOP] == borders[BOTTOM]
        assert tile.borders[BOTTOM] == borders[TOP]
        assert tile.borders[LEFT] == flipped_borders[LEFT]
        assert tile.borders[RIGHT] == flipped_borders[RIGHT]

    def test_tile_flip_v(self):
        tile = Tile(TILE_2311.splitlines())

        borders = tile.borders.copy()
        flipped_borders = tile.flipped_borders.copy()

        tile.flip_v()
        assert tile.borders[TOP] == flipped_borders[TOP]
        assert tile.borders[BOTTOM] == flipped_borders[BOTTOM]
        assert tile.borders[RIGHT] == borders[LEFT]
        assert tile.borders[LEFT] == borders[RIGHT]

    def test_tile_flip_d(self):
        tile = Tile(TILE_2311.splitlines())

        flipped_borders = tile.flipped_borders.copy()

        tile.flip_d()

        assert tile.borders[TOP] == flipped_borders[RIGHT]
        assert tile.borders[RIGHT] == flipped_borders[TOP]
        assert tile.borders[BOTTOM] == flipped_borders[LEFT]
        assert tile.borders[LEFT] == flipped_borders[BOTTOM]

    def test_invert_rotation(self):
        tile = Tile(TILE_2311.splitlines())

        tile.borders = [0, 1, 2, 3]
        tile._update_flipped()

        tile.flip_h()
        tile.flip_v()
        tile.flip_d()

        expected = [3, 2, 1, 0]
        self.assertEqual(expected, tile.borders)


    def test_rotated_alignment(self):
        tile = Tile(TILE_2311.splitlines())

        tile.borders = [1, 2, 3, 4]
        tile._update_flipped()

        tile.rotate()
        tile.flip_h()

        alignments = []
        alignments.append((LEFT, 1))
        alignments.append((TOP, 4))

        tile.align(alignments)

        expected = [4, 3, 2, 1]
        self.assertEqual(expected, tile.borders)


    def test_tile_rotate(self):
        tile = Tile(TILE_2311.splitlines())
        borders = tile.borders.copy()

        tile.rotate()
        assert tile.borders[RIGHT] == borders[TOP]
        assert tile.borders[BOTTOM] == borders[RIGHT]
        assert tile.borders[LEFT] == borders[BOTTOM]
        assert tile.borders[TOP] == borders[LEFT]


    def test_tile_borderless(self):
        tile = Tile(TILE_2311.splitlines())
        expected = """\
#..#....
...##..#
###.#...
#.##.###
#...#.##
#.#.#..#
.#....#.
##...#.#
""".splitlines()

        actual = list("".join(row) for row in tile.borderless())
        self.assertListEqual(expected, actual)


    def test_print_image(self):
        lines = get_resource(f'day_{DAY}/example_1.txt').read_text().splitlines()
        puzzle = Puzzle(lines)

        solution = [
            [ 1951, 2311, 3079 ],
            [ 2729, 1427, 2473 ],
            [ 2971, 1489, 1171 ],
        ]
        puzzle.rotate()
        puzzle.flip_d()
        puzzle.rotate(3)

        actual = list(
            list(tile.id for tile in row) for row in puzzle.matrix
        )
        self.assertListEqual(solution, actual)

        tile = Tile(TILE_2311.splitlines())
        tile.flip_h()
        self.assertEqual(tile.id, puzzle.matrix[0][1].id)
        self.assertListEqual(tile.pixels, puzzle.matrix[0][1].pixels)

        image = Image(puzzle)
        img = str(image).splitlines()
        assert len(img) == 8 * 3
        assert len(img[0]) == 8 * 3
        s_image = str(image)
        e_image = get_resource(f'day_{DAY}/example_image.txt').read_text().strip()
        self.assertEqual(e_image, s_image)


    def test_find_monsters(self):
        lines = get_resource(f'day_{DAY}/example_1.txt').read_text().splitlines()
        puzzle = Puzzle(lines)
        image = Image(puzzle)

        self.assertListEqual(image.pixels[0], list(".####...#####..#...###.."))

        expected = 2
        actual = image.find_monsters()
        self.assertEqual(expected, actual)

        expected_monsters = get_resource(f'day_{DAY}/detected_monsters.txt').read_text().splitlines()
        actual_monsters = str(image).splitlines()
        self.assertListEqual(expected_monsters, actual_monsters)


    def test_find_lone_monster(self):
        lines = get_resource(f'day_{DAY}/example_1.txt').read_text().splitlines()
        puzzle = Puzzle(lines)
        image = Image(puzzle)

        image.pixels = [
            list(row) for row in MONSTER
        ]

        expected = 1
        actual = image.find_monsters()
        self.assertEqual(expected, actual)

        image.pixels = [
            list(repeat('#', 20)) for _ in MONSTER
        ]
        actual = image.find_monsters()
        self.assertEqual(expected, actual)



    def test_roughness(self):
        lines = get_resource(f'day_{DAY}/example_1.txt').read_text().splitlines()
        puzzle = Puzzle(lines)
        image = Image(puzzle)

        self.assertListEqual(image.pixels[0], list(".####...#####..#...###.."))
        image.find_monsters()


        expected = 273
        actual = image.roughness()
        self.assertEqual(expected, actual)


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

    def test_rotate(self):
        original = [
            [ 1951, 2311, 3079 ],
            [ 2729, 1427, 2473 ],
            [ 2971, 1489, 1171 ],
        ]
        expected = [
            [ 2971, 2729, 1951 ],
            [ 1489, 1427, 2311 ],
            [ 1171, 2473, 3079 ],
        ]
        actual = rotate(original)
        self.assertListEqual(expected, actual)


    def test_solve_matrix_positions(self):
        expected = [
            [ 1951, 2311, 3079 ],
            [ 2729, 1427, 2473 ],
            [ 2971, 1489, 1171 ],
        ]

        lines = get_resource(f'day_{DAY}/example_1.txt').read_text().splitlines()
        puzzle = Puzzle(lines)
        puzzle.find_corners()
        puzzle.find_edges()
        actual = puzzle.solve_matrix(puzzle.tiles[1951])
        tile_ids = list(list(
           t.id for t in row
        ) for row in actual)
        tile_ids = rotate(tile_ids)
        tile_ids = flip_v(tile_ids)
        self.assertListEqual(expected, tile_ids)


    def test_answer_2(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
        puzzle = Puzzle(lines)

        answer = find_roughness(puzzle)
        assert answer != -1
        print(f'\nAnswer 2 : {answer}\n')

        assert answer < 2521
        assert answer > 2236


        # expected =
        # self.assertEqual(expected, answer)

