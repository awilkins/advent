import pytest

from ..util import get_resource_lines


from advent.day_11.passwords import *

DAY = "11"

EXAMPLE_ONE = """\
The next password after abcdefgh is abcdffaa
The next password after ghijklmn is ghjaabcc
""".splitlines()


class TestPartOne:
    pass

    def test_straight(self):
        assert contains_straight("hijklmmn")

    def test_confusing(self):
        assert confusing_chars("hijklmmn")

    def test_pairs(self):
        assert has_enough_pairs("abbceffg")

    @pytest.mark.parametrize('line', EXAMPLE_ONE)
    def test_example_1(self, line:str):
        expected = line.split()[6]
        actual = answer_1(line.split()[4])
        assert expected == actual

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines[0])
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
        answer = answer_2(lines[0])
        print(f'\nAnswer 2 : {answer}\n')
        # expected =
        # assert expected == answer
