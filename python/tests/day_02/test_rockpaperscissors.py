from unittest import TestCase

from ..util import get_resource

DAY="02"

from advent.day_02.rockpaperscissors import *

EXAMPLE_INPUT = """\
A Y
B X
C Z
"""

class TestThing(TestCase):

    def test_rock_beats_scissors(self):
        self.assertEqual(7, score('C', 'X'))



    def test_example_1(self):
        lines = EXAMPLE_INPUT.splitlines()
        expected = 15
        actual = answer_1(lines)
        self.assertEqual(expected, actual)

    def test_example_2(self):
        lines = EXAMPLE_INPUT.splitlines()
        expected = 12
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

