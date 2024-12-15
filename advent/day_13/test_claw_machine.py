import pytest

from ..util import get_resource_lines


from advent.day_13.claw_machine import (
    answer_1,
    answer_2,
    machines,
)

DAY = "13"

EXAMPLE_ONE = """\
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
""".splitlines()


class TestPartOne:
    pass

    def test_parse(self):
        m = machines(EXAMPLE_ONE)
        assert (94, 34) == m[0].button_a
        assert (22, 67) == m[0].button_b
        assert (8400, 5400) == m[0].prize

        assert (18641, 10279) == m[3].prize
        assert 4 == len(m)

    def test_solve(self):
        m = machines(EXAMPLE_ONE)
        m0 = m[0]

        assert 280 == m0.solve()

    def test_example_1(self):
        lines = EXAMPLE_ONE
        expected = 480
        actual = answer_1(lines)
        assert expected == actual

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines)
        print(f"\nAnswer 1 : {answer}\n")
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
