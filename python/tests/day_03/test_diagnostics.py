from unittest import TestCase

from ..util import get_resource

DAY="03"

from advent.day_03.diagnostics import *

EXAMPLE_INPUT = """\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""

class TestThing(TestCase):

    def test_example_1(self):
        lines = EXAMPLE_INPUT.splitlines()

        expected = 198
        actual = answer_1(lines)

        self.assertEqual(expected, actual)

    def test_answer_1(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        answer = answer_1(lines)
        print(f'\nAnswer 1 : {answer}\n')

        expected = 2261546
        self.assertEqual(expected, answer)

    def test_example_2(self):
        lines = EXAMPLE_INPUT.splitlines()

        expected = 230
        actual = answer_2(lines)

        self.assertEqual(expected, actual)


    def test_answer_2(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        answer = answer_2(lines)
        print(f'\nAnswer 2 : {answer}\n')

        expected = 6775520
        self.assertEqual(expected, answer)

