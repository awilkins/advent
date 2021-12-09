from unittest import TestCase

from ..util import get_resource

DAY="09"

from advent.day_09.tubes import *

EXAMPLE_INPUT = """\
2199943210
3987894921
9856789892
8767896789
9899965678
"""

class TestThing(TestCase):

    def test_example_1(self):
        lines = EXAMPLE_INPUT.splitlines()

        m = make_map(lines)

        self.assertTrue(is_low(m, 1, 0))
        self.assertTrue(is_low(m, 9, 0))
        self.assertTrue(is_low(m, 2, 2))
        self.assertTrue(is_low(m, 6, 4))

        self.assertFalse(is_low(m, 0, 1))
        self.assertFalse(is_low(m, 1, 1))
        self.assertFalse(is_low(m, 9, 4))

        actual = map_risk(m)
        expected = 15

        self.assertEqual(expected, actual)

    def test_answer_1(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        answer = answer_1(lines)
        print(f'\nAnswer 1 : {answer}\n')

        expected = 506
        self.assertEqual(expected, answer)


    def test_basins(self):
        lines = EXAMPLE_INPUT.splitlines()
        m = make_map(lines)

        self.assertEqual(3, len(basin(m, 1, 0)))
        self.assertEqual(9, len(basin(m, 9, 0)))
        self.assertEqual(14, len(basin(m, 2, 2)))
        self.assertEqual(9, len(basin(m, 6, 4)))

        self.assertEqual(answer_2(lines), 1134)


    def test_answer_2(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        answer = answer_2(lines)
        print(f'\nAnswer 2 : {answer}\n')

        expected = 931200
        self.assertEqual(expected, answer)

