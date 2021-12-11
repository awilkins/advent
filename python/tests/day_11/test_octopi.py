from unittest import TestCase

from ..util import get_resource

DAY="11"

from advent.day_11.octopi import *

EXAMPLE_INPUT = """\
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""

class TestThing(TestCase):

    def test_example_1(self):
        lines = EXAMPLE_INPUT.splitlines()
        m = make_map(lines)

        expected = 1656
        actual = cycle_map(m, 100)

        self.assertEqual(expected, actual)

    def test_answer_1(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        m = make_map(lines)
        answer = cycle_map(m, 100)
        print(f'\nAnswer 1 : {answer}\n')

        expected = 1669
        self.assertEqual(expected, answer)

    def test_example_2(self):
        lines = EXAMPLE_INPUT.splitlines()
        m = make_map(lines)

        expected = 195
        actual = first_flash(m)

        self.assertEqual(expected, actual)


    def test_answer_2(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
        m = make_map(lines)

        answer = first_flash(m)

        print(f'\nAnswer 2 : {answer}\n')

        expected = 351
        self.assertEqual(expected, answer)

