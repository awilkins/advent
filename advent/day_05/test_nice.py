import pytest

from ..util import get_resource_lines


from advent.day_05.nice import *

DAY = "05"

NICE = """\
ugknbfddgicrmopn
aaa
""".splitlines()

NAUGHTY = """\
jchzalrnumimnmhp
haegwjzuvuyypxyu
dvszwmarrgswjxmb
"""


class TestPartOne:
    pass

    @pytest.mark.parametrize("line", NICE)
    def test_nice(self, line):
        assert is_nice(line)

    @pytest.mark.parametrize("line", NAUGHTY)
    def test_naughty(self, line):
        assert not is_nice(line)

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines)
        print(f"\nAnswer 1 : {answer}\n")
        # expected =
        # assert expected == answer


EXAMPLE_TWO = NICE


class TestPartTwo:
    pass

    def test_double_couplet(self):
        assert contains_double_couplet("xxyxx")
        assert not contains_double_couplet("xxx")
        assert contains_double_couplet("xxxx")

    def test_blinky_repeat(self):
        assert contains_blinky_repeat("xyx")
        assert contains_blinky_repeat("xxyxx")
        assert not contains_blinky_repeat("xyyx")

    NICER = [
        "qjhvhtzxzqqjkmpb",
        "xxyxx",
    ]


    @pytest.mark.parametrize("line", NICER)
    def test_nicer(self, line):
        assert is_nicer(line)


    NAUGHTIER = ["uurcxstgmygtbstg", "ieodomkazucvgmuy"]

    @pytest.mark.parametrize("line", NAUGHTIER)
    def test_naughtier(self, line):
        assert not is_nicer(line)

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
