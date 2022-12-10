from unittest import TestCase

from ..util import get_resource

DAY="09"

from advent.day_09.bridge import *

EXAMPLE_INPUT = """\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

EXAMPLE_TWO_LONG="""\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""

class TestThing(TestCase):


    def test_tail(self):
        rope = Rope(1, (-2, 0))
        rope.follow()
        self.assertEqual((-1, 0), rope.tail)


    def test_example_1(self):
        lines = EXAMPLE_INPUT.splitlines()
        expected = 13
        actual = answer_1(lines)
        self.assertEqual(expected, actual)

    def test_example_2(self):
        lines = EXAMPLE_INPUT.splitlines()
        expected = 1
        actual = answer_2(lines)
        self.assertEqual(expected, actual)

    def test_example_2_long(self):
        lines = EXAMPLE_TWO_LONG.splitlines()
        expected = 36
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

