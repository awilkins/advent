from unittest import TestCase

from ..util import get_resource

DAY="10"

from advent.day_10.adapters import *

EXAMPLE_INPUT = """\
16
10
15
5
1
12
11
7
19
6
4
"""

EXAMPLE_2 = """\
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""

class TestAnswer1(TestCase):

    def test_example_1(self):
        input_lines = EXAMPLE_INPUT.splitlines()

        expected = 7 * 5
        actual = product(input_lines)

        self.assertEqual(expected, actual)

    def test_example_2(self):
        input_lines = EXAMPLE_2.splitlines()

        expected = 22 * 10
        actual = product(input_lines)

        self.assertEqual(expected, actual)

    def test_answer_1(self):
        input_lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        expected = 2176
        answer = product(input_lines)
        self.assertEqual(expected, answer)
        print(f'\nAnswer 1 : {answer}\n')

EXAMPLE_2_1 = """\
(0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 6, 7, 10,     12, 15, 16, 19, (22)
(0), 1, 4, 5,    7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 5,    7, 10,     12, 15, 16, 19, (22)
(0), 1, 4,    6, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4,    6, 7, 10,     12, 15, 16, 19, (22)
(0), 1, 4,       7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4,       7, 10,     12, 15, 16, 19, (22)
"""

EXAMPLE_2_2 = """
(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49, (52)
(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 47,     49, (52)
(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46,     48, 49, (52)
(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46,         49, (52)
(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45,     47, 48, 49, (52)
(0),       3, 4, 7,       10, 11, 14, 17,         20, 23,     25, 28, 31,         34, 35, 38, 39, 42, 45, 46,     48, 49, (52)
(0),       3, 4, 7,       10, 11, 14, 17,         20, 23,     25, 28, 31,         34, 35, 38, 39, 42, 45, 46,         49, (52)
(0),       3, 4, 7,       10, 11, 14, 17,         20, 23,     25, 28, 31,         34, 35, 38, 39, 42, 45,     47, 48, 49, (52)
(0),       3, 4, 7,       10, 11, 14, 17,         20, 23,     25, 28, 31,         34, 35, 38, 39, 42, 45,     47,     49, (52)
(0),       3, 4, 7,       10, 11, 14, 17,         20, 23,     25, 28, 31,         34, 35, 38, 39, 42, 45,         48, 49, (52)
"""

class TestAnswer2(TestCase):

    def test_can_omit(self):
        input_lines = EXAMPLE_INPUT.splitlines()
        adapters = list([int(x) for x in input_lines])
        adapters.sort()
        expected = [5, 6, 11]
        actual = can_omit(adapters)
        actual_values = list([adapters[ii] for ii in actual])
        self.assertListEqual(expected, actual_values)

        input_lines = EXAMPLE_2.splitlines()
        adapters = list([int(x) for x in input_lines])
        adapters.append(0)
        adapters.sort()
        adapters.append(adapters[-1] + 3)
        omit_2 = can_omit(adapters)
        omissions = list([adapters[x] for x in omit_2])
        print(f'\nExample 2 contains : {adapters} ({len(adapters)})')
        print(f'Example 2 can omit : {omissions} ({len(omit_2)})')
        self.assertIn(48, omissions)

    def test_example_1(self):
        input_lines = EXAMPLE_INPUT.splitlines()

        expected = 8
        actual = arrangements(input_lines)

        self.assertEqual(expected, actual)

    def test_example_2(self):
        input_lines = EXAMPLE_2.splitlines()

        expected = 19208
        actual = arrangements(input_lines)

        self.assertEqual(expected, actual)

    def test_answer_2(self):
        input_lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        # expected =
        answer = arrangements(input_lines)
        # self.assertEqual(expected, answer)
        print(f'\nAnswer 2 : {answer}\n')

