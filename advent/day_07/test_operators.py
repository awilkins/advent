import pytest

from ..util import get_resource_lines


from advent.day_07.operators import (
    Equation,
    answer_1,
    answer_2,
    parse,
    solve,
)


DAY = "07"

EXAMPLE_ONE = """\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
""".splitlines()


class TestPartOne:
    pass

    def test_parse(self):
        equations: list[Equation] = parse(EXAMPLE_ONE)

        assert (190, [10, 19]) == equations[0]
        assert (292, [11, 6, 16, 20]) == equations[8]

    def test_solve(self):
        equations: list[Equation] = parse(EXAMPLE_ONE)

        eq = equations[0]
        result = solve(eq, list("+"))
        assert result == 29
        result = solve(eq, list("*"))
        assert result == 190

        eq = equations[1]
        result = solve(eq, list("+*"))
        assert result == 3267
        result = solve(eq, list("*+"))
        assert result == 3267

    def test_example_1(self):
        lines = EXAMPLE_ONE
        expected = 3749
        actual = answer_1(lines)
        assert expected == actual

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines)
        print(f"\nAnswer 1 : {answer}\n")
        expected = 882304362421
        assert expected == answer


EXAMPLE_TWO = EXAMPLE_ONE


class TestPartTwo:
    pass

    def test_example_2(self):
        lines = EXAMPLE_TWO
        expected = 11387
        actual = answer_2(lines)
        assert expected == actual

    def test_answer_2(self):
        lines = get_resource_lines(DAY)
        answer = answer_2(lines)
        print(f"\nAnswer 2 : {answer}\n")
        # expected =
        # assert expected == answer
