from unittest import TestCase

from ..util import get_resource

DAY="01"

from advent.day_01.depth import *

EXAMPLE_INPUT = """\
199
200
208
210
200
207
240
269
260
263
"""

class TestThing(TestCase):

    def test_example_1(self):
        lines = EXAMPLE_INPUT.splitlines()

        expected = 7
        actual = depth_increases(lines)

        self.assertEqual(expected, actual)

    def test_answer_1(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        answer = depth_increases(lines)
        print(f'\nAnswer 1 : {answer}\n')

        # expected =
        # self.assertEqual(expected, answer)

    def test_example_2(self):
        lines = EXAMPLE_INPUT.splitlines()

        expected = 5
        actual = depth_windows(lines)

        self.assertEqual(expected, actual)

    def test_answer_2(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        answer = depth_windows(lines)
        print(f'\nAnswer 2 : {answer}\n')

    #     # expected =
    #     # self.assertEqual(expected, answer)

