import pytest

from ..util import get_resource_lines


from advent.day_02.reports import *

DAY="02"

EXAMPLE_ONE = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".splitlines()

class TestPartOne:
    pass

    def test_is_safe(self):
        reports = get_reports(EXAMPLE_ONE)

        assert is_safe(reports[0])
        assert not is_safe(reports[1])
        assert not is_safe(reports[2])
        assert not is_safe(reports[3])
        assert not is_safe(reports[4])
        assert is_safe(reports[5])

    def test_example_1(self):
        lines = EXAMPLE_ONE
        expected = 2
        actual = answer_1(lines)
        assert expected == actual

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines)
        print(f'\nAnswer 1 : {answer}\n')
        expected = 314
        assert expected == answer


EXAMPLE_TWO = EXAMPLE_ONE

class TestPartTwo:
    pass

    def test_dampen(self):
        report = [1, 2, 3, 4, 5]
        assert [1, 3, 4, 5] == dampen(report, 1)
        assert [2, 3, 4, 5] == dampen(report, 0)

    def test_example_2(self):
        lines = EXAMPLE_TWO
        expected = 4
        actual = answer_2(lines)
        assert expected == actual

    def test_answer_2(self):
        lines = get_resource_lines(DAY)
        answer = answer_2(lines)
        print(f'\nAnswer 2 : {answer}\n')
    #     # expected =
    #     # assert expected == answer

