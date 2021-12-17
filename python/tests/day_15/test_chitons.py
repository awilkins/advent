from unittest import TestCase
from unittest.case import skip

from ..util import get_resource

DAY="15"

from advent.day_15.chitons import *

EXAMPLE_INPUT = """\
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""

class TestThing(TestCase):

    def test_example_1(self):
        lines = EXAMPLE_INPUT.splitlines()
        expected = 40
        actual = answer_1(lines)
        self.assertEqual(expected, actual)

    def test_example_2(self):
        lines = EXAMPLE_INPUT.splitlines()
        expected = 315
        actual = answer_2(lines)
        self.assertEqual(expected, actual)

    def test_answer_1(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
        answer = answer_1(lines)
        print(f'\nAnswer 1 : {answer}\n')
        expected = 717
        self.assertEqual(expected, answer)

    def test_answer_2(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
        answer = answer_2(lines)
        print(f'\nAnswer 2 : {answer}\n')
        # expected =
        # self.assertEqual(expected, answer)

