from unittest import TestCase

from ..util import get_resource

DAY="03"

from advent.day_03.rucksack import *

EXAMPLE_INPUT = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

class TestThing(TestCase):

    def test_common_item(self):
        expected = 'a'
        actual = common_item('pacMan')
        self.assertEqual(expected, actual)

    def test_scores(self):
        self.assertEqual(22, score('v'))
        self.assertEqual(38, score('L'))

    def test_example_1(self):
        lines = EXAMPLE_INPUT.splitlines()
        expected = 157
        actual = answer_1(lines)
        self.assertEqual(expected, actual)

    def test_groups(self):
        lines = EXAMPLE_INPUT.splitlines()
        g = list(groups(lines))

        self.assertEqual(2, len(g))
        self.assertEqual('r', group_item(g[0]))
        self.assertEqual('Z', group_item(g[1]))

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

