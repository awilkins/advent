import pytest

from ..util import get_resource_lines


from advent.day_15.lens_library import *

DAY = "15"

EXAMPLE_ONE = """\
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
""".splitlines()


class TestPartOne:
    pass

    def test_hash(self):
        assert hash("HASH") == 52

    # def test_example_1(self):
    #     lines = EXAMPLE_ONE
    #     expected =
    #     actual = answer_1(lines)
    #     assert expected == actual

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines)
        print(f"\nAnswer 1 : {answer}\n")
        expected = 495972
        assert expected == answer


EXAMPLE_TWO = EXAMPLE_ONE


class TestPartTwo:
    pass

    def test_example_2(self):
        lines = EXAMPLE_TWO
        expected = 145
        actual = answer_2(lines)
        assert expected == actual

    def test_answer_2(self):
        lines = get_resource_lines(DAY)
        answer = answer_2(lines)
        print(f"\nAnswer 2 : {answer}\n")
        expected = 245223
        assert expected == answer
