import pytest

from ..util import get_resource_lines


from advent.day_06.boat_race import *


EXAMPLE_ONE = """\
Time:      7  15   30
Distance:  9  40  200
""".splitlines()


class TestPartOne:
    pass

    def test_race_distance(self):
        assert race_distance(7, 1) == 6

    def test_winners(self):
        assert race_winners(7, 9) == 4
        assert race_winners(15, 40) == 8

    def test_example_1(self):
        lines = EXAMPLE_ONE
        expected = 288
        actual = answer_1(lines)
        assert expected == actual

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines)
        print(f"\nAnswer 1 : {answer}\n")
        expected = 211904
        assert expected == answer


EXAMPLE_TWO = EXAMPLE_ONE


class TestPartTwo:
    pass

    # def test_example_2(self):
    #     lines = EXAMPLE_TWO
    #     expected =
    #     actual = answer_2(lines)
    #     assert expected == actual

    def test_answer_2(self):
        lines = get_resource_lines(DAY)
        answer = answer_2(lines)
        print(f"\nAnswer 2 : {answer}\n")
        expected = 43364472
        assert expected == answer
