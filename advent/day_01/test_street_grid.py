import pytest

from ..util import get_resource_lines, get_resource_string


from advent.day_01.street_grid import (
    Dude,
    answer_1,
    answer_2,
)

DAY = "01"

EXAMPLE_ONE = """\
R2, L3:5
R2, R2, R2:2
R5, L5, R5, R3:12
""".splitlines()


class TestPartOne:
    def test_move_right(self):
        dude = Dude()
        dude.move_right(5)
        assert (5, 0) == dude.position

    def test_move_right_then_right(self):
        dude = Dude()
        dude.move_right(5)
        dude.move_right(5)
        assert (5, -5) == dude.position

    def test_move_left(self):
        dude = Dude()
        dude.move_left(3)  # west , -3
        dude.move_left(4)  # south, -4
        assert (-3, -4) == dude.position

    def test_example_1(self):
        lines = EXAMPLE_ONE
        for line in lines:
            [input, expected] = line.split(":")
            expected = int(expected)
            actual = answer_1(input)
            assert expected == actual

    def test_answer_1(self):
        lines = get_resource_string(DAY)
        answer = answer_1(lines)
        print(f"\nAnswer 1 : {answer}\n")
        # expected =
        # assert expected == answer


EXAMPLE_TWO = "R8, R4, R4, R8"


class TestPartTwo:
    def test_example_2(self):
        lines = EXAMPLE_TWO
        expected = 4
        actual = answer_2(lines)
        assert expected == actual

    def test_answer_2(self):
        line = get_resource_string(DAY)
        answer = answer_2(line)
        print(f"\nAnswer 2 : {answer}\n")
        # expected =
        # assert expected == answer
