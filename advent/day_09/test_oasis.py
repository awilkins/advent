import pytest

from ..util import get_resource_lines


from advent.day_09.oasis import *

DAY = "09"

EXAMPLE_ONE = """\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""".splitlines()


class TestPartOne:
    pass

    def test_line_progression(self):
        line = OasisLine(EXAMPLE_ONE[0])
        line.extend()
        assert line.next_value() == 18

        line2 = OasisLine(EXAMPLE_ONE[1])
        line2.extend()
        assert line2.next_value() == 28

        line3 = OasisLine(EXAMPLE_ONE[2])
        line3.extend()
        assert line3.next_value() == 68

    def test_example_1(self):
        lines = EXAMPLE_ONE
        expected = 114
        actual = answer_1(lines)
        assert expected == actual

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines)
        print(f"\nAnswer 1 : {answer}\n")
        assert answer < 1785385884
        expected = 1782868781
        assert expected == answer


EXAMPLE_TWO = EXAMPLE_ONE


class TestPartTwo:
    pass

    def test_example_2(self):
        lines = EXAMPLE_TWO
        expected = 2
        actual = answer_2(lines)
        assert expected == actual

    def test_answer_2(self):
        lines = get_resource_lines(DAY)
        answer = answer_2(lines)
        print(f"\nAnswer 2 : {answer}\n")
        expected = 1057
        assert expected == answer
