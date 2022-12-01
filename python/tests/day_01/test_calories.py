from unittest import TestCase

from ..util import get_resource

DAY="01"

from advent.day_01.calories import *

EXAMPLE_INPUT = """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

class TestCalories(TestCase):

    def test_example_1(self):
        lines = EXAMPLE_INPUT.splitlines()
        expected = 24000
        actual = largest_calories(lines)
        self.assertEqual(expected, actual)

    def test_example_2(self):
        lines = EXAMPLE_INPUT.splitlines()
        expected = 45000
        actual = answer_2(lines)
        self.assertEqual(expected, actual)

    def test_answer_1(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
        answer = answer_1(lines)
        print(f'\nAnswer 1 : {answer}\n')
        # expected =
        # self.assertEqual(expected, answer)

    def test_answer_2(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
        answer = answer_2(lines)
        print(f'\nAnswer 2 : {answer}\n')
        # expected =
        # self.assertEqual(expected, answer)

