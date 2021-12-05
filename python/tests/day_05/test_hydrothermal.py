from unittest import TestCase
from unittest.case import expectedFailure

from ..util import get_resource

DAY="05"

from advent.day_05.hydrothermal import *

EXAMPLE_INPUT = """\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""

class TestThing(TestCase):

    def test_points(self):
        v = Vector("0,9 -> 5,9")
        actual = v.points()
        expected = [
            (0, 9),
            (1, 9),
            (2, 9),
            (3, 9),
            (4, 9),
            (5, 9),
        ]
        for index, p in enumerate(actual):
            self.assertTupleEqual(expected[index], p)


    def test_example_1(self):
        lines = EXAMPLE_INPUT.splitlines()

        expected = 5
        actual = answer_1(lines)

        self.assertEqual(expected, actual)

    def test_answer_1(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        answer = answer_1(lines, 1000)
        print(f'\nAnswer 1 : {answer}\n')

        expected = 6225
        self.assertEqual(expected, answer)

    def test_example_2(self):
        lines = EXAMPLE_INPUT.splitlines()

        expected = 12
        actual = answer_2(lines)

        self.assertEqual(expected, actual)

    def test_answer_2(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        answer = answer_2(lines, 1000)
        print(f'\nAnswer 2 : {answer}\n')

        expected = 22116
        self.assertEqual(expected, answer)

