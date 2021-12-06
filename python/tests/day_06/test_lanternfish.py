from advent.day_06.lanternfish import *
from unittest import TestCase

from ..util import get_resource

DAY = "06"


EXAMPLE_INPUT = """\
3,4,3,1,2
"""

EXAMPLE_OUTPUT = """\
Initial state: 3,4,3,1,2
After  1 day:  2,3,2,0,1
After  2 days: 1,2,1,6,0,8
After  3 days: 0,1,0,5,6,7,8
After  4 days: 6,0,6,4,5,6,7,8,8
After  5 days: 5,6,5,3,4,5,6,7,7,8
After  6 days: 4,5,4,2,3,4,5,6,6,7
After  7 days: 3,4,3,1,2,3,4,5,5,6
After  8 days: 2,3,2,0,1,2,3,4,4,5
After  9 days: 1,2,1,6,0,1,2,3,3,4,8
After 10 days: 0,1,0,5,6,0,1,2,2,3,7,8
After 11 days: 6,0,6,4,5,6,0,1,1,2,6,7,8,8,8
After 12 days: 5,6,5,3,4,5,6,0,0,1,5,6,7,7,7,8,8
After 13 days: 4,5,4,2,3,4,5,6,6,0,4,5,6,6,6,7,7,8,8
After 14 days: 3,4,3,1,2,3,4,5,5,6,3,4,5,5,5,6,6,7,7,8
After 15 days: 2,3,2,0,1,2,3,4,4,5,2,3,4,4,4,5,5,6,6,7
After 16 days: 1,2,1,6,0,1,2,3,3,4,1,2,3,3,3,4,4,5,5,6,8
After 17 days: 0,1,0,5,6,0,1,2,2,3,0,1,2,2,2,3,3,4,4,5,7,8
After 18 days: 6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8
"""


class TestThing(TestCase):

    def test_next_day(self):

        fish = [int(f) for f in EXAMPLE_INPUT.split(',')]

        actual = format_fish(fish, 0)
        expected = EXAMPLE_OUTPUT.splitlines()[0]
        self.assertEqual(actual, expected)

        for day in range(1, 19):
            fish = next_day(fish)
            actual = format_fish(fish, day)
            expected = EXAMPLE_OUTPUT.splitlines()[day]
            self.assertEqual(actual, expected)
            print(actual, len(fish))

    def test_example_1(self):
        lines = EXAMPLE_INPUT.splitlines()

        expected = 26
        actual = answer_1(lines, 18)

        self.assertEqual(actual, expected)

        expected = 5934
        actual = answer_1(lines, 80)

        self.assertEqual(actual, expected)

    def test_answer_1(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        answer = answer_1(lines, 80)
        print(f'\nAnswer 1 : {answer}\n')

        expected = 359999
        self.assertEqual(expected, answer)

    def test_example_2(self):
        lines = EXAMPLE_INPUT.splitlines()

        expected = 26
        actual = answer_2(lines, 18)

        self.assertEqual(actual, expected)

        expected = 5934
        actual = answer_2(lines, 80)

        self.assertEqual(actual, expected)

    def test_answer_1_with_solution_2(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        answer = answer_2(lines, 80)

        expected = 359999
        self.assertEqual(expected, answer)

    def test_answer_2(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        answer = answer_2(lines, 256)
        print(f'\nAnswer 2 : {answer}\n')

        expected = 1631647919273
        self.assertEqual(expected, answer)
