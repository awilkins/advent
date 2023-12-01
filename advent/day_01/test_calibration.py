from unittest import TestCase
import pytest

from ..util import get_resource_lines

DAY = "01"

from advent.day_01.calibration import *

EXAMPLE_INPUT = """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""


class TestPartOne:

    def test_find_first_digit(self):
        assert find_first_digit("abc123") == "1"

    def test_find_last_digit(self):
        assert find_last_digit("abc123") == "3"

    def test_example_1(self):
        lines = EXAMPLE_INPUT.splitlines()
        expected = 142
        actual = answer_1(lines)
        assert expected == actual

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines)
        print(f"\nAnswer 1 : {answer}\n")
        # expected =
        # assert expected == answer


EXAMPLE_TWO = """\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""


class TestPartTwo:

    @pytest.mark.parametrize("line,expected", [
        ("two1nine", ['2', '1', '9']),
        ("eighttwothree", ['8', '2', '3']),
        ("abcone2threexyz", ['1', '2', '3']),
        ("xtwone3four", ['2','1','3','4']),
        ("4nineeightseven2", ['4', '9', '8', '7', '2']),
        ("zoneight234", ['1', '8', '2', '3', '4']),
        ("7pqrstsixteen", ["7", "16"]),
    ])
    def test_find_digits(self, line, expected):
        actual = find_digits(line)
        assert expected == actual

    @pytest.mark.parametrize("line,expected", [
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
    ])
    def test_find_number_2(self, line, expected):
        assert find_number_2(line) == expected

    def test_example_2(self):
        lines = EXAMPLE_TWO.splitlines()
        expected = 281
        actual = answer_2(lines)
        assert expected == actual

    def test_answer_2(self):
        lines = get_resource_lines(DAY)
        answer = answer_2(lines)
        print(f'\nAnswer 2 : {answer}\n')
        # expected =
        # self.assertEqual(expected, answer)
