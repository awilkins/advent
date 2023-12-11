import pytest

from ..util import get_resource_lines


from advent.day_11.galaxies import *

DAY="11"

EXAMPLE_ONE = """\
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
""".splitlines()

class TestPartOne:
    pass
    
    def test_distance(self):
        gal_5 = Position(1, 6)
        gal_9 = Position(5, 11)
        assert gal_5.distance(gal_9) == 9

    def test_example_1(self):
        lines = EXAMPLE_ONE
        expected = 374
        actual = answer_1(lines)
        assert expected == actual

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines)
        print(f'\nAnswer 1 : {answer}\n')
        expected = 9274989
        assert expected == answer


EXAMPLE_TWO = EXAMPLE_ONE

class TestPartTwo:
    pass

    def test_example_2(self):
        lines = EXAMPLE_TWO
        expected = 1030
        actual = answer_2(lines, 10)
        assert expected == actual

    def test_example_3(self):
        lines = EXAMPLE_TWO
        expected = 8410
        actual = answer_2(lines, 100)
        assert expected == actual

    def test_answer_2(self):
        lines = get_resource_lines(DAY)
        answer = answer_2(lines, 1_000_000)
        print(f'\nAnswer 2 : {answer}\n')
        expected = 357134560737
        assert expected == answer

