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

        map = make_map(lines)

        self.assertTrue(is_low(map, 1, 0))
        self.assertTrue(is_low(map, 9, 0))
        self.assertTrue(is_low(map, 2, 2))
        self.assertTrue(is_low(map, 4, 6))

        self.assertFalse(is_low(map, 0, 1))
        self.assertFalse(is_low(map, 1, 1))
        self.assertFalse(is_low(map, 9, 4))

        actual = map_risk(map)
        expected = 15

        self.assertEqual(expected, actual)

    def test_answer_1(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        answer = answer_1(lines)
        print(f'\nAnswer 1 : {answer}\n')

        # expected =
        # self.assertEqual(expected, answer)

    # def test_answer_2(self):
    #     lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

    #     answer =
    #     print(f'\nAnswer 2 : {answer}\n')

    #     # expected =
    #     # self.assertEqual(expected, answer)

