from unittest import TestCase

from ..util import get_resource

DAY="01"

from advent.day_01.rocket_fuel import *

EXAMPLE_INPUT = """\
"""

class TestThing(TestCase):

    def test_example_1(self):
        lines = EXAMPLE_INPUT.splitlines()
        expected =
        actual = answer_1(lines)
        self.assertEqual(expected, actual)

    # def test_example_2(self):
    #     lines = EXAMPLE_INPUT.splitlines()
    #     expected =
    #     actual = answer_2(lines)
    #     self.assertEqual(expected, actual)

    # def test_answer_1(self):
    #     lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
    #     answer = answer_1(lines)
    #     print(f'\nAnswer 1 : {answer}\n')
    #     # expected =
    #     # self.assertEqual(expected, answer)

    # def test_answer_2(self):
    #     lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
    #     answer = answer_2(lines)
    #     print(f'\nAnswer 2 : {answer}\n')
    #     # expected =
    #     # self.assertEqual(expected, answer)

