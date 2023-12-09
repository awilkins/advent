import pytest

from ..util import get_resource_lines


from advent.day_16.aunt_sue import *

DAY="16"

EXAMPLE_ONE = """\
""".splitlines()

FINGERLINES = """\
children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
""".splitlines()

class TestPartOne:
    pass



    # def test_example_1(self):
    #     lines = EXAMPLE_ONE
    #     expected =
    #     actual = answer_1(lines)
    #     assert expected == actual

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines, FINGERLINES)
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
        answer = answer_2(lines, FINGERLINES)
        print(f'\nAnswer 2 : {answer}\n')
        # expected =
        # assert expected == answer

