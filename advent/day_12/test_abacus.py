import pytest

from ..util import get_resource_lines


from advent.day_12.abacus import *

DAY="12"

EXAMPLE_ONE = """\
[1,2,3]
{"a":2,"b":4}
[[[3]]]
{"a":{"b":4},"c":-1}
{"a":[-1,1]}
[-1,{"a":1}]
[]
{}
""".splitlines()

class TestPartOne:
    pass

    @pytest.mark.parametrize('line,expected', [
        (EXAMPLE_ONE[0], 6),
        (EXAMPLE_ONE[1], 6),
        (EXAMPLE_ONE[2], 3),
        (EXAMPLE_ONE[3], 3),
        (EXAMPLE_ONE[4], 0),
        (EXAMPLE_ONE[5], 0),
        (EXAMPLE_ONE[6], 0),
        (EXAMPLE_ONE[7], 0),
    ])
    def test_example_1(self, line, expected):
        actual = answer_1(line)
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

