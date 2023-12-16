import pytest

from ..util import get_resource_lines


from advent.day_19.medicine import *

DAY="19"

EXAMPLE_ONE = """\
""".splitlines()

REPLACEMENTS = (
    ('H', 'HO'),
    ('H', 'OH'),
    ('O', 'HH'),
)

class TestPartOne:
    pass

    def test_hoh(self):
        assert mutation_count('HOH', REPLACEMENTS) == 4

    def test_hohoho(self):
        assert mutation_count('HOHOHO', REPLACEMENTS) == 7

    # def test_example_1(self):
    #     li
    #     expected = 7
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

    def test_answer_2(self):
        lines = get_resource_lines(DAY)
        answer = answer_2(lines)
        print(f'\nAnswer 2 : {answer}\n')
        # expected =
        # assert expected == answer

