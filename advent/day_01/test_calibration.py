import pytest

from ..util import get_resource, get_resource_lines

from .calibration import *

DAY = "01"

EXAMPLE_ONE = """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

EXAMPLE_LINES = EXAMPLE_ONE.splitlines()


def test_first_char_is_one():
    assert EXAMPLE_ONE[0] == "1"


@pytest.mark.parametrize(
    "line,value",
    [
        (EXAMPLE_LINES[0], 12),
        (EXAMPLE_LINES[1], 38),
        (EXAMPLE_LINES[2], 15),
        (EXAMPLE_LINES[3], 77),
    ],
)
def test_line_values(line, value):
    assert line_value(line) == value


def test_example_one():
    assert answer_1(EXAMPLE_LINES) == 142


def test_answer_one():
    lines = get_resource_lines(DAY)
    answer = answer_1(lines)
    print(f"\nAnswer 1 : {answer}")
    assert answer == 55607


EXAMPLE_TWO = """\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
""".splitlines()

def test_two_one_nine():
    line = EXAMPLE_TWO[0]
    assert line_value(line) == 29

@pytest.mark.parametrize('line,value', [
    (EXAMPLE_TWO[0], 29),
    (EXAMPLE_TWO[1], 83),
    (EXAMPLE_TWO[2], 13),
    (EXAMPLE_TWO[3], 24),
    (EXAMPLE_TWO[4], 42),
    (EXAMPLE_TWO[5], 14),
    (EXAMPLE_TWO[6], 76),
])
def test_line_values_with_words(line, value):
    assert line_value(line) == value

def test_line_value_with_twelve():
    assert line_value('3twelve') == 32

def test_six_is_six():
    assert digit_value('six') == 6

def test_example_2():
    assert answer_2(EXAMPLE_TWO) == 281


def test_answer_two():
    lines = get_resource_lines(DAY)
    answer = answer_2(lines)
    print(f"\nAnswer 2 : {answer}")
    assert answer == 55291
