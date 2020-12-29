from unittest import TestCase

from ..util import get_resource

DAY="24"

from advent.day_24.hex_tiles import *

EXAMPLE_INPUT = """\
sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
"""

class TestFloor(TestCase):


    def test_example_1(self):
        lines = EXAMPLE_INPUT.splitlines()

        expected = 10

        floor = Floor()
        actual = floor.lay_tiles(lines)

        self.assertEqual(expected, actual)


    def test_answer_1(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        floor = Floor()
        answer = floor.lay_tiles(lines)
        print(f'\nAnswer 1 : {answer}\n')

        expected = 322
        self.assertEqual(expected, answer)


    def test_example_2(self):
        lines = EXAMPLE_INPUT.splitlines()

        expected = 10

        floor = Floor()
        actual = floor.lay_tiles(lines)

        self.assertEqual(expected, actual)

        floor.tick()
        self.assertEqual(15, floor.count_black())
        floor.tick()
        self.assertEqual(12, floor.count_black())

        for ii in range(98):
            floor.tick()

        self.assertEqual(2208, floor.count_black())


    def test_neighbours(self):

        floor = Floor()

        one = Coord((1, 1))

        actual = floor.get_neighbours(one)
        expected = [
            (1, 0),
            (2, 0),
            (0, 1),
            (2, 1),
            (1, 2),
            (2, 2),
        ]
        for e in expected:
            self.assertIn(e, actual)

        two = Coord((2, 2))
        actual = floor.get_neighbours(two)
        expected = [
            (1, 1),
            (2, 1),
            (1, 2),
            (3, 2),
            (1, 3),
            (2, 3),
        ]
        for e in expected:
            self.assertIn(e, actual)


    def test_answer_2(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        floor = Floor()
        floor.lay_tiles(lines)

        for _ in range(100):
            floor.tick()

        answer = floor.count_black()
        print(f'\nAnswer 2 : {answer}\n')

        expected = 3831
        self.assertEqual(expected, answer)

