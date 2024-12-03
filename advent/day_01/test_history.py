import pytest

from ..util import get_resource_string, get_resource_lines


from advent.day_01.history import *

DAY="01"

EXAMPLE_ONE = """\
3   4
4   3
2   5
1   3
3   9
3   3
""".splitlines()

class TestPartOne:
    pass

    def test_get_lists(self):
        input = EXAMPLE_ONE

        list_1, list_2 = get_lists(input)
        assert [3, 4, 2, 1, 3, 3] == list_1
        assert [4, 3, 5, 3, 9, 3] == list_2

    def test_example_1(self):
        lines = EXAMPLE_ONE
        expected = 11
        actual = answer_1(lines)
        assert expected == actual

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines)
        print(f'\nAnswer 1 : {answer}\n')
    #     # expected =
    #     # assert expected == answer


EXAMPLE_TWO = EXAMPLE_ONE

class TestPartTwo:
    pass

    def test_item_count(self):
        _, list_2 = get_lists(EXAMPLE_TWO)
        assert 3 == item_count(3, list_2)
        assert 1 == item_count(4, list_2)


    def test_example_2(self):
        lines = EXAMPLE_TWO
        expected = 31
        actual = answer_2(lines)
        assert expected == actual

    def test_answer_2(self):
        lines = get_resource_lines(DAY)
        answer = answer_2(lines)
        print(f'\nAnswer 2 : {answer}\n')
    #     # expected =
    #     # assert expected == answer

