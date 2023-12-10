import pytest

from ..util import get_resource_lines


from advent.day_17.eggnog import *

DAY="17"

EXAMPLE_ONE = """\
20
15
10
5
5
""".splitlines()

class TestPartOne:
    pass

    def test_example_1(self):
        lines = EXAMPLE_ONE
        expected = 4
        actual = answer_1(lines, 25)
        assert expected == actual

    # def test_answer_1(self):
    #     lines = get_resource_lines(DAY)
    #     answer = answer_1(lines)
    #     print(f'\nAnswer 1 : {answer}\n')
    #     # expected =
    #     # assert expected == answer


EXAMPLE_TWO = EXAMPLE_ONE

class TestPartTwo:
    pass

    # def test_example_2(self):
    #     lines = EXAMPLE_TWO
    #     expected =
    #     actual = answer_2(lines)
    #     assert expected == actual

    # def test_answer_2(self):
    #     lines = get_resource_lines(DAY)
    #     answer = answer_2(lines)
    #     print(f'\nAnswer 2 : {answer}\n')
    #     # expected =
    #     # assert expected == answer

