from unittest import TestCase

from ..util import get_resource

DAY="21"

from advent.day_21.dirac import *

EXAMPLE_INPUT = """\
"""

class TestThing(TestCase):

    def test_example_1(self):
        expected = 739785
        actual = answer_1(4, 8)
        self.assertEqual(expected, actual)

    # def test_example_2(self):
    #     lines = EXAMPLE_INPUT.splitlines()
    #     expected =
    #     actual =
    #     self.assertEqual(expected, actual)

    def test_answer_1(self):
        answer = answer_1(3, 5)
        print(f'\nAnswer 1 : {answer}\n')
        # expected =
        # self.assertEqual(expected, answer)

    # def test_answer_2(self):
    #     lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
    #     answer = answer_2(lines)
    #     print(f'\nAnswer 2 : {answer}\n')
    #     # expected =
    #     # self.assertEqual(expected, answer)

