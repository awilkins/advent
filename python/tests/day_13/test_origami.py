from unittest import TestCase

from ..util import get_resource

DAY="13"

from advent.day_13.origami import *

EXAMPLE_INPUT = """\
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""

class TestThing(TestCase):

    def test_example_1(self):
        lines = EXAMPLE_INPUT.splitlines()
        expected = 17
        actual = answer_1(lines)
        self.assertEqual(expected, actual)


    def test_example_2(self):
        lines = EXAMPLE_INPUT.splitlines()
        answer_2(lines)

    def test_answer_1(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
        answer = answer_1(lines)
        print(f'\nAnswer 1 : {answer}\n')
        # expected =
        # self.assertEqual(expected, answer)

    def test_answer_2(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
        answer = ""
        print(f'\nAnswer 2 : {answer}\n')
        answer_2(lines)
        # expected =
        # self.assertEqual(expected, answer)

