from unittest import TestCase

from ..util import get_resource

DAY="04"

from advent.day_04.cleaning import *

EXAMPLE_INPUT = """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

class TestThing(TestCase):

    def test_example_1(self):
        lines = EXAMPLE_INPUT.splitlines()
        expected = 2
        actual = answer_1(lines)
        self.assertEqual(expected, actual)

    # def test_example_2(self):
    #     lines = EXAMPLE_INPUT.splitlines()
    #     expected =
    #     actual = answer_2(lines)
    #     self.assertEqual(expected, actual)

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

