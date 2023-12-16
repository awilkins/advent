import pytest

from ..util import get_resource_lines


from advent.day_18.game_of_lights import *

DAY="18"

EXAMPLE_ONE = """\
.#.#.#
...##.
#....#
..#...
#.#..#
####..
""".splitlines()

NINE = """\
...
...
...
""".splitlines()

class TestPartOne:
    pass

    def test_neighbour_count(self):
        w = World(EXAMPLE_ONE)
        assert len(w.neighbours(Position(1, 1))) == 8
        assert len(w.neighbours(Position(0, 0))) == 3


    def test_example_1(self):
        lines = EXAMPLE_ONE
        expected = 4
        actual = answer_1(lines, 4)
        assert expected == actual

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines, 100)
        print(f'\nAnswer 1 : {answer}\n')
        # expected =
        # assert expected == answer


EXAMPLE_TWO = EXAMPLE_ONE

class TestPartTwo:
    pass

    def test_example_2(self):
        lines = EXAMPLE_TWO
        expected = 17
        actual = answer_2(lines, 5)
        assert expected == actual

    def test_answer_2(self):
        lines = get_resource_lines(DAY)
        answer = answer_2(lines, 100)
        print(f'\nAnswer 2 : {answer}\n')
        # expected =
        # assert expected == answer

