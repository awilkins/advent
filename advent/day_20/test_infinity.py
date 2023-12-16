import pytest

from ..util import get_resource_lines


from advent.day_20.infinity import *

DAY="20"

EXAMPLE_ONE = """\
""".splitlines()

class TestPartOne:
    pass

    def test_gift_count(self):
        assert gift_count(1) == 10
        assert gift_count(2) == 30
        assert gift_count(3) == 40

    def test_house_1(self):
        assert house_number(10) == 1

    def test_house_2(self):
        assert house_number(30) == 2
        assert house_number(31) == 2

    # def test_example_1(self):
    #     lines = EXAMPLE_ONE
    #     expected =
    #     actual = answer_1(lines)
    #     assert expected == actual

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines)
        print(f'\nAnswer 1 : {answer}\n')
        # expected =
        # assert expected == answer


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

