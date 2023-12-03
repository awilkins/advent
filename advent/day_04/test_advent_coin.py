import pytest

from ..util import get_resource_lines


from advent.day_04.advent_coin import *

DAY = "04"

EXAMPLE_ONE = """\
""".splitlines()


class TestPartOne:
    pass

    def test_example_1(self):
        assert 609043 == find_block("abcdef")

    def test_example_2(self):
        assert 1048970 == find_block("pqrstuv")

    def test_answer_1(self):
        answer = answer_1("ckczppom")
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
        answer = find_block("ckczppom", 6)
        print(f'\nAnswer 2 : {answer}\n')
        # expected =
        # assert expected == answer
