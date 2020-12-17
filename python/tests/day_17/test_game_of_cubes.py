from unittest import TestCase

from ..util import get_resource

DAY="17"

from advent.day_17.game_of_cubes import *

EXAMPLE_INPUT = """\
.#.
..#
###
"""

class TestThing(TestCase):

    def test_neighbours(self):

        zero: Coord = Coord((0, 0, 0, 0))

        cube = Cube(zero)
        nb = cube.neighbours()

        self.assertEqual(26, len(nb))


    def test_example_1(self):
        plane = parse_plane(EXAMPLE_INPUT.splitlines())

        space = CubeSpace(plane)

        actual = space.count()
        expected = 5

        self.assertEqual(expected, actual)
        print(space)


    def test_cycles(self):
        plane = parse_plane(EXAMPLE_INPUT.splitlines())

        space = CubeSpace(plane)

        for ii in range(3):
            with self.subTest(cycle=ii+1):
                expected = get_resource(f'day_17/cycle_{ii+1}.txt').read_text()
                space = space.cycle()
                actual = str(space)
                self.assertMultiLineEqual(expected, actual)


    def test_answer_1(self):
        plane = parse_plane(get_resource(f'day_{DAY}/input.txt').read_text().splitlines())

        space = CubeSpace(plane)
        ii = 0

        while ii < 6:
            space = space.cycle()
            ii += 1

        answer = space.count()

        print(f'\nAnswer 1 : {answer}\n')

        expected = 298
        self.assertEqual(expected, answer)

    def test_answer_2(self):
        plane = parse_plane(get_resource(f'day_{DAY}/input.txt').read_text().splitlines())

        space = CubeSpace(plane, dimensions = 4)
        ii = 0

        while ii < 6:
            space = space.cycle()
            ii += 1

        answer = space.count()

        print(f'\nAnswer 2 : {answer}\n')

        expected = 848
        self.assertEqual(expected, answer)


    def test_cycles_4d(self):
        plane = parse_plane(EXAMPLE_INPUT.splitlines())

        space = CubeSpace(plane, dimensions = 4)

        for ii in range(2):
            with self.subTest(cycle=ii+1):
                expected = get_resource(f'day_17/cycle_4d_{ii+1}.txt').read_text()
                space = space.cycle()
                actual = str(space)
                self.assertMultiLineEqual(expected, actual)
