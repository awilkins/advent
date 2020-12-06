from unittest import TestCase

from advent.day_06.customs import group_count, group_set_count
from tests.util import get_resource


EXAMPLE_GROUP = """\
abcx
abcy
abcz
"""

EXAMPLE_GROUP_SET = """\
abc

a
b
c

ab
ac

a
a
a
a

b
"""


class TestCustoms(TestCase):


    def test_example_group(self):
        lines = EXAMPLE_GROUP.splitlines()

        expected = 6
        actual = group_count(lines)
        self.assertEqual(expected, actual)

    def test_example_group_set(self):
        lines = EXAMPLE_GROUP_SET.splitlines()

        expected = 11
        actual = group_set_count(lines)
        self.assertEqual(expected, actual)


    def test_answer_1(self):
        lines = get_resource('day_06/input.txt').read_text().splitlines()

        print(f'\nAnswer 01 : {group_set_count(lines)}')


    def test_example_2(self):
        lines = EXAMPLE_GROUP_SET.splitlines()

        expected = 6
        actual = group_set_count(lines, all=True)
        self.assertEqual(expected, actual)


    def test_answer_2(self):
        lines = get_resource('day_06/input.txt').read_text().splitlines()

        print(f'\nAnswer 01 : {group_set_count(lines, all=True)}')
