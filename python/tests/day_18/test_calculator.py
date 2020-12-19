from unittest import TestCase

from ..util import get_resource

DAY="18"

from advent.day_18.calculator import *

EXAMPLE_INPUT = "1 + 2 * 3 + 4 * 5 + 6"

class TestThing(TestCase):

    def test_example_1(self):
        input_lines = EXAMPLE_INPUT.splitlines()

        expected = 71
        actual = evaluate(input_lines[0])

        self.assertEqual(expected, actual)

    def test_parens(self):
        line = "1 + (2 * 3) + (4 * (5 + 6))"

        expected = 51
        actual = evaluate(line)

        self.assertEqual(expected, actual)

    def test_answer_1(self):
        input_lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        answer = sum(evaluate(line) for line in input_lines)
        print(f'\nAnswer 1 : {answer}\n')

        expected = 131076645626
        self.assertEqual(expected, answer)

    def test_precedence_2(self):

        actual = maffs_2("1 + 2 * 3 + 4 * 5 + 6")
        expected = 231

        self.assertEqual(expected, actual)

    def test_examples_2(self):
        expressions = [
            ("1 + (2 * 3) + (4 * (5 + 6))", 51),
            ("2 * 3 + (4 * 5)", 46),
            ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 1445),
            ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 669060),
            ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 23340),
        ]

        for expression, expected in expressions:
            with self.subTest(expression=expression):
                self.assertEqual(expected, maffs_2(expression))

    def test_answer_2(self):
        input_lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        answer = sum(maffs_2(line) for line in input_lines)
        print(f'\nAnswer 2 : {answer}\n')

        expected = 109418509151782
        self.assertEqual(expected, answer)

