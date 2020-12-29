from unittest import TestCase

from ..util import get_resource

DAY="25"

from advent.day_25.loopy_crypto import *

EXAMPLE_INPUT = """\
"""

DOOR = 1526110
CARD = 20175123


class TestThing(TestCase):

    def test_loop(self):

        self.assertEqual(5764801, loop(7, 8))
        self.assertEqual(8, find_loop_size(5764801))
        self.assertEqual(11, find_loop_size(17807724))


    def test_key(self):
        expected = 14897079
        actual = find_encryption_key(17807724, 5764801)

        self.assertEqual(expected, actual)

    # def test_example_1(self):
    #     lines = EXAMPLE_INPUT.splitlines()

    #     expected =
    #     actual =

    #     self.assertEqual(expected, actual)

    def test_answer_1(self):
        answer = find_encryption_key(DOOR, CARD)
        print(f'\nAnswer 1 : {answer}\n')

        # expected =
        # self.assertEqual(expected, answer)

    # def test_answer_2(self):
    #     input_lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

    #     answer =
    #     print(f'\nAnswer 2 : {answer}\n')

    #     # expected =
    #     # self.assertEqual(expected, answer)

