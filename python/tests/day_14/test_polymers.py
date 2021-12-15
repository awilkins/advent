from unittest import TestCase
from unittest.case import skip

from ..util import get_resource

DAY="14"

from advent.day_14.polymers import *

EXAMPLE_INPUT = """\
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""

class TestThing(TestCase):

    def test_example_1(self):
        lines = EXAMPLE_INPUT.splitlines()
        poly = make_chain(lines[0])
        rules = make_rules(lines[2:])
        step_1 = get_next_poly(poly, rules)

        expected = "NCNBCHB"
        actual = str(step_1)
        self.assertEqual(expected, actual)

        expected = "NBCCNBBBCBHCB"
        self.assertEqual(expected, str(get_next_poly(poly, rules)))

        self.assertEqual(1588, answer_1(lines))
        self.assertEqual(1588, answer_2(lines))

    def test_example_2(self):
        lines = EXAMPLE_INPUT.splitlines()
        expected = 2188189693529
        actual = answer_2(lines, 40)
        self.assertEqual(expected, actual)

    def test_answer_1(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
        answer = answer_1(lines)
        print(f'\nAnswer 1 : {answer}\n')
        expected = 2027
        self.assertEqual(expected, answer)
        self.assertEqual(expected, answer_2(lines))

    def test_answer_2(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
        answer = answer_2(lines, 40)
        print(f'\nAnswer 2 : {answer}\n')
        # expected =
        # self.assertEqual(expected, answer)

