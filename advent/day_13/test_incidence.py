import pytest

from ..util import get_resource_lines


from advent.day_13.incidence import *

DAY="13"

EXAMPLE_ONE = """\
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
""".splitlines()

class TestPartOne:
    pass

    def test_vertical_reflection(self):
        lines = EXAMPLE_ONE[0:7]
        p = Pattern(lines)
        assert p.is_vertical_reflection(5)
        assert not p.is_vertical_reflection(4)
        assert p.find_reflection() == (5, 0)
        
    def test_horizontal_reflection(self):
        lines = EXAMPLE_ONE[8:]
        p = Pattern(lines)
        assert p.is_horizontal_reflection(4)
        assert p.find_reflection() == (0, 4)
    
    def test_example_1(self):
        lines = EXAMPLE_ONE
        expected = 405
        actual = answer_1(lines)
        assert expected == actual

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines)
        print(f'\nAnswer 1 : {answer}\n')
        # expected =
        # assert expected == answer


EXAMPLE_TWO = EXAMPLE_ONE

class TestPartTwo:
    pass

    def test_second_pattern_other(self):
        lines = EXAMPLE_ONE[8:]
        p = Pattern(lines)
        assert p.is_horizontal_reflection(4)
        assert p.find_reflection() == (0, 4)
        assert get_new_reflection(p) == (0, 1)
        
    def test_example_2(self):
        lines = EXAMPLE_TWO
        expected = 400
        actual = answer_2(lines)
        assert expected == actual

    def test_answer_2(self):
        lines = get_resource_lines(DAY)
        answer = answer_2(lines)
        print(f'\nAnswer 2 : {answer}\n')
        # expected =
        # assert expected == answer

