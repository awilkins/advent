import pytest

from ..util import get_resource_lines


from advent.day_10.looksay import *

DAY="10"

EXAMPLE_ONE = """\
1 11
11 21
21 1211
1211 111221
111221 312211
""".splitlines()

class TestPartOne:
    pass

    @pytest.mark.parametrize('line', EXAMPLE_ONE)
    def test_example_1(self, line):
        input, expected = line.split()
        actual = looksay(input)
        assert expected == actual

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines[0])
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

    def test_answer_2(self):
        lines = get_resource_lines(DAY)
        answer = answer_2(lines[0])
        print(f'\nAnswer 2 : {answer}\n')
        # expected =
        # assert expected == answer

