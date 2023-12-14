import pytest

from ..util import get_resource_lines


from advent.day_12.springs import *

DAY = "12"

EXAMPLE_ONE = """\
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
""".splitlines()


class TestPartOne:
    pass

    def test_arragements(self):
        assert possible_arrangements("???.### 1,1,3") == 1

    def test_example_1(self):
        lines = EXAMPLE_ONE
        expected = 21
        actual = answer_1(lines)
        assert expected == actual

    # @pytest.mark.skip('slow')
    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines)
        print(f"\nAnswer 1 : {answer}\n")
        expected = 7732
        assert expected == answer


EXAMPLE_TWO = EXAMPLE_ONE


class TestPartTwo:
    pass

    def test_expansion(self):
        assert expanded(".# 1") == ".#?.#?.#?.#?.# 1,1,1,1,1"

    def test_arrangements_2(self):
        assert 2500 == possible_arrangements_2(expanded("????.######..#####. 1,6,5"))



    def test_estimate(self):
        estimate_2(get_resource_lines(DAY))

    def test_example_2(self):
        lines = EXAMPLE_TWO
        expected = 525152
        actual = answer_2(lines)
        assert expected == actual

    def test_answer_2(self):
        lines = get_resource_lines(DAY)
        answer = answer_2(lines)
        print(f"\nAnswer 2 : {answer}\n")
        # expected =
        # assert expected == answer
