from unittest import TestCase

import pytest

from ..util import get_resource

DAY="08"

from advent.day_08.tree_house import *

EXAMPLE_INPUT = """\
30373
25512
65332
33549
35390
"""

@pytest.mark.parametrize("input,expected",
    [
        ((1, 1), True),
        ((2, 1), True),
        ((3, 1), False),
        ((1, 2), True),
        ((2, 2), False),
        ((3, 2), True),
        ((1, 3), False),
        ((2, 3), True),
        ((3, 3), False),
    ]
)
def test_visible(input, expected):
    lines = EXAMPLE_INPUT.splitlines()
    trees = parse_trees(lines)
    actual = is_visible(trees, input)
    assert expected == actual

def test_example_1():
    lines = EXAMPLE_INPUT.splitlines()
    expected = 21
    actual = answer_1(lines)
    assert expected == actual

@pytest.mark.parametrize("input,expected",
    [
        ((2, 1), 4),
        ((2, 3), 8),
    ]
)
def test_score(input, expected):
    lines = EXAMPLE_INPUT.splitlines()
    trees = parse_trees(lines)
    actual = scenic_score(trees, input)
    assert expected == actual

def test_example_2():
    lines = EXAMPLE_INPUT.splitlines()
    expected = 8
    actual = answer_2(lines)
    assert expected == actual

def test_answer_1():
    lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
    answer = answer_1(lines)
    print(f'\nAnswer 1 : {answer}\n')
    # expected =
    # self.assertEqual(expected, answer)

def test_answer_2():
    lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
    answer = answer_2(lines)
    print(f'\nAnswer 2 : {answer}\n')
    # expected =
    # self.assertEqual(expected, answer)

