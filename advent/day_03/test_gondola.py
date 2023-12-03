import pytest

from ..util import get_resource_lines

DAY = "03"

from advent.day_03.gondola import *

EXAMPLE_ONE = """\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".splitlines()


class TestPartOne:
    pass

    @pytest.mark.parametrize('input, expected', [
        (EXAMPLE_ONE[0], [467, 114]),
        (EXAMPLE_ONE[1], []),
        ('.....123', [ 123 ]),
    ])
    def test_find_number_groups(self, input, expected):
        assert find_number_groups(input) == expected



    # def test_example_1(self):
    #     lines = EXAMPLE_ONE
    #     expected =
    #     actual = answer_1(lines)
    #     assert expected == actual

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
    #     lines = EXAMPLE_TWO.splitlines()
    #     expected =
    #     actual = answer_2(lines)
    #     assert expected == actual

    # def test_answer_2(self):
    #     lines = get_resource_lines(DAY)
    #     answer = answer_2(lines)
    #     print(f'\nAnswer 2 : {answer}\n')
    #     # expected =
    #     # assert expected == answer
