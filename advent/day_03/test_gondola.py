import pytest

from itertools import chain

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


#       0123456789
#
# 00  : 467..114..
# 01  : ...*......
# 02  : ..35..633.
# 03  : ......#...
# 04  : 617*......
# 05  : .....+.58.
# 06  : ..592.....
# 07  : ......755.
# 08  : ...$.*....
# 09  : .664.598..
#

EDGE_ONE = """\
..........
..........
..........
......*...
.......123
""".splitlines()

EDGE_TWO = """\
.......123
......*...
..........
..........
..........
""".splitlines()

EDGE_THREE = """\
..........
..........
..........
...*......
123.......
""".splitlines()

EDGE_FOUR = """\
123.......
...*......
..........
..........
..........
""".splitlines()


class TestPartOne:
    pass

    @pytest.mark.parametrize(
        "input, expected",
        [
            (EXAMPLE_ONE[0], [(467, 0), (114, 5)]),
            (EXAMPLE_ONE[1], []),
            (".....123", [(123, 5)]),
        ],
    )
    def test_find_number_groups(self, input, expected):
        assert find_number_groups(input) == expected

    ALL_NUMBERS = get_all_numbers(EXAMPLE_ONE)

    NUMBERS_WITH_SYMBOLS = [
        number for number in ALL_NUMBERS if number[0] not in [114, 58]
    ]

    # @pytest.mark.skip
    @pytest.mark.parametrize("input", NUMBERS_WITH_SYMBOLS)
    def test_component_has_adjacent_symbol(self, input):
        c = Component()
        c.number, c.x, c.y = input[0], input[1][0], input[1][1]
        assert c.has_adjacent_symbol(EXAMPLE_ONE)

    # @pytest.mark.skip
    @pytest.mark.parametrize("input", NUMBERS_WITH_SYMBOLS)
    def test_has_adjacent_symbol(self, input):
        assert has_adjacent_symbol(EXAMPLE_ONE, input)

    @pytest.mark.parametrize("input", [(114, (5, 0)), (58, (7, 5))])
    def test_has_no_adjacent_symbol(self, input):
        assert not has_adjacent_symbol(EXAMPLE_ONE, input)

    @pytest.mark.parametrize("input", [(114, (5, 0)), (58, (7, 5))])
    def test_component_has_no_adjacent_symbol(self, input):
        c = Component()
        c.number, c.x, c.y = input[0], input[1][0], input[1][1]
        assert not c.has_adjacent_symbol(EXAMPLE_ONE)

    def test_example_1(self):
        lines = EXAMPLE_ONE
        expected = 4361
        actual = answer_1(lines)
        assert expected == actual

    def test_example_1_c(self):
        lines = EXAMPLE_ONE
        expected = 4361
        actual = answer_1_c(lines)
        assert expected == actual

    @pytest.mark.parametrize(
        "input",
        [
            EDGE_ONE,
            EDGE_TWO,
            EDGE_THREE,
            EDGE_FOUR,
        ],
    )
    def test_edges(self, input):
        lines = input
        expected = 123
        actual = answer_1(lines)
        assert expected == actual

    def test_do_digits_count_as_symbols(self):
        TEST_GRID = """\
        ..........
        ..........
        ...123....
        ......321.
        ..........
        """.splitlines()

        assert answer_1(TEST_GRID) == 0

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines)
        print(f"\nAnswer 1 : {answer}\n")
        expected = 544664
        assert expected == answer


EXAMPLE_TWO = EXAMPLE_ONE


class TestPartTwo:
    pass

    def test_example_2(self):
        lines = EXAMPLE_TWO
        expected = 467835
        actual = answer_2(lines)
        assert expected == actual

    def test_answer_2(self):
        lines = get_resource_lines(DAY)
        answer = answer_2(lines)
        print(f'\nAnswer 2 : {answer}\n')
        # expected =
        # assert expected == answer
