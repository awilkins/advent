import pytest

from ..util import get_resource_lines

from collections import deque


from advent.day_11.pebbles import (
    answer_1,
    answer_2,
    blink,
)

DAY = "11"

EXAMPLE_ONE = """\
125 17
253000 1 7
253 0 2024 14168
512072 1 20 24 28676032
512 72 2024 2 0 2 4 2867 6032
1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32
2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2
""".splitlines()


class TestPartOne:
    pass

    def test_blink(self):
        for ii in range(len(EXAMPLE_ONE) - 1):
            expected = deque(int(n) for n in EXAMPLE_ONE[ii + 1].split())
            actual = blink(deque(int(n) for n in EXAMPLE_ONE[ii].split()))
            assert expected == actual

    def test_example_1(self):
        lines = EXAMPLE_ONE
        expected = 55312
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

    def test_answer_2(self):
        lines = get_resource_lines(DAY)
        answer = answer_2(lines)
        print(f"\nAnswer 2 : {answer}\n")
        # expected =
        # assert expected == answer
