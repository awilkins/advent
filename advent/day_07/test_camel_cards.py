import pytest

from ..util import get_resource_lines


from advent.day_07.camel_cards import *

DAY = "07"

EXAMPLE_ONE = """\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".splitlines()


class TestPartOne:
    pass

    def test_hand_class(self):
        assert FIVE == hand_class("AAAAA")
        assert FOUR == hand_class("AA8AA")
        assert FULL_HOUSE == hand_class("23332")
        assert THREE == hand_class("TTT98")
        assert TWO_PAIR == hand_class("23432")
        assert PAIR == hand_class("32T3K")
        assert HIGH == hand_class("23456")

    def test_hand_sort(self):
        hands = [line.split()[0] for line in EXAMPLE_ONE]
        hands.sort(key=hand_key)
        assert hands == [
            "32T3K",
            "KTJJT",
            "KK677",
            "T55J5",
            "QQQJA",
        ]

    def test_example_1(self):
        lines = EXAMPLE_ONE
        expected = 6440
        actual = answer_1(lines)
        assert expected == actual

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines)
        print(f"\nAnswer 1 : {answer}\n")
        expected = 251029473
        assert expected == answer


EXAMPLE_TWO = EXAMPLE_ONE


class TestPartTwo:
    pass

    def test_hand_class(self):
        assert FOUR == hand_class("KTJJT", True)

    def test_hand_sort(self):
        hands = [line.split()[0] for line in EXAMPLE_ONE]
        hands.sort(key=lambda x: hand_key(x, True))
        assert hands == [
            "32T3K",
            "KK677",
            "T55J5",
            "QQQJA",
            "KTJJT",
        ]

    def test_example_2(self):
        lines = EXAMPLE_TWO
        expected = 5905
        actual = answer_2(lines)
        assert expected == actual

    def test_answer_2(self):
        lines = get_resource_lines(DAY)
        answer = answer_2(lines)
        print(f"\nAnswer 2 : {answer}\n")
        expected = 251003917
        assert expected == answer
