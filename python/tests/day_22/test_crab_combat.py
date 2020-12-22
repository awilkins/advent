from unittest import TestCase

from ..util import get_resource

DAY="22"

from advent.day_22.crab_combat import *

EXAMPLE_INPUT = """\
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
"""

class TestThing(TestCase):

    def test_example_1(self):
        lines = EXAMPLE_INPUT.splitlines()

        expected = 306
        actual = play_combat(lines)

        self.assertEqual(expected, actual)

    def test_answer_1(self):
        input_lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        answer = play_combat(input_lines)
        print(f'\nAnswer 1 : {answer}\n')

        # expected =
        # self.assertEqual(expected, answer)

    # def test_answer_2(self):
    #     input_lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

    #     answer =
    #     print(f'\nAnswer 2 : {answer}\n')

    #     # expected =
    #     # self.assertEqual(expected, answer)

