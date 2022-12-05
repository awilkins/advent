from unittest import TestCase

from ..util import get_resource

DAY="05"

from advent.day_05.crates import *

EXAMPLE_INPUT = "" + \
"    [D]    \n" + \
"[N] [C]    \n" + \
"[Z] [M] [P]\n" + \
" 1   2   3\n" + \
"\n" + \
"move 1 from 2 to 1\n" + \
"move 3 from 1 to 3\n" + \
"move 2 from 2 to 1\n" + \
"move 1 from 1 to 2\n"


class TestThing(TestCase):

    def test_example_1(self):
        lines = EXAMPLE_INPUT.splitlines()
        expected = "CMZ"
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

