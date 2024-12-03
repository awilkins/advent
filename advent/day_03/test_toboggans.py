import pytest

from ..util import *


import advent.day_03.toboggans as t
from advent.day_03.toboggans import *

DAY="03"

EXAMPLE_ONE = """\
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""

class TestPartOne:
    pass

    def test_find_muls(self):
        expected = [
            (2, 4),
            (5, 5),
            (11, 8),
            (8, 5)
        ]

        def get_instructions(p): return [(b, c) for _, b, c in t.get_instructions(p)]

        assert [(2, 4)] == get_instructions("mul(2,4)")
        assert [(5, 5)] == get_instructions("mul(5,5)")
        assert [(11, 8)] == get_instructions("mul(11,8)")

        assert expected == get_instructions(EXAMPLE_ONE)

    def test_example_1(self):
        lines = EXAMPLE_ONE
        expected = 161
        actual = answer_1(lines)
        assert expected == actual

    def test_answer_1(self):
        program = get_resource_string(DAY)
        answer = answer_1(program)
        print(f'\nAnswer 1 : {answer}\n')
        expected = 153469856
        assert expected == answer


EXAMPLE_TWO = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

class TestPartTwo:
    pass

    def test_parse_dont(self):

        ins = get_instructions(EXAMPLE_TWO, support_dodont=True)
        assert ("mul(2,4)", 2, 4) == ins[0]
        assert DONT == ins[1]

    def test_example_2(self):
        lines = EXAMPLE_TWO
        expected = 48
        actual = answer_2(lines)
        assert expected == actual

    def test_answer_2(self):
        lines = get_resource_string(DAY)
        answer = answer_2(lines)
        print(f'\nAnswer 2 : {answer}\n')
        expected = 77055967
        assert expected == answer
