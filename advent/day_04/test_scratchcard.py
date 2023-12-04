import pytest

from ..util import get_resource_lines

DAY = "04"

from advent.day_04.scratchcard import *

EXAMPLE_ONE = """\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
""".splitlines()


class TestPartOne:
    pass

    @pytest.mark.parametrize(
        "line,score",
        [
            (EXAMPLE_ONE[0], 8),
            (EXAMPLE_ONE[1], 2),
            (EXAMPLE_ONE[2], 2),
            (EXAMPLE_ONE[3], 1),
            (EXAMPLE_ONE[4], 0),
            (EXAMPLE_ONE[5], 0),
        ],
    )
    def test_example_1(self, line, score):
        card = Card(line)
        assert card.score() == score
        assert card.number > 0

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines)
        print(f"\nAnswer 1 : {answer}\n")
        expected = 23678
        assert expected == answer


EXAMPLE_TWO = EXAMPLE_ONE


class TestPartTwo:
    pass

    def test_example_2(self):
        lines = EXAMPLE_TWO
        expected = 30
        actual = answer_2(lines)
        assert expected == actual

    def test_answer_2(self):
        lines = get_resource_lines(DAY)
        answer = answer_2(lines)
        print(f"\nAnswer 2 : {answer}\n")
        expected = 15455663
        assert expected == answer
