import pytest

from ..util import get_resource_lines


from advent.day_01.safedial import (
    Safe,
    answer_1,
    answer_2,
)

DAY = "01"

EXAMPLE_ONE = """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
""".splitlines()


class TestPartOne:
    pass

    def test_rotate(self):
        safe = Safe(11)
        safe.rotate("R8")
        assert safe.dial == 19

        safe.rotate("L19")
        assert safe.dial == 0

    def test_rotate_wraps(self):
        safe = Safe(0)
        assert 99 == safe.rotate("L1")
        assert 0 == safe.rotate("R1")

    def test_more(self):
        safe = Safe(5)
        assert safe.rotate("L10") == 95
        assert safe.rotate("R5") == 0

    def test_safe_starts_at_50(self):
        safe = Safe()
        assert safe.dial == 50

    def test_example_1(self):
        lines = EXAMPLE_ONE
        expected = 3
        actual = answer_1(lines)
        assert expected == actual

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines)
        print(f"\nAnswer 1 : {answer}\n")
        # expected =
        # assert expected == answer


EXAMPLE_TWO = EXAMPLE_ONE


class TestPartTwo:
    pass

    # Each time the dial hits 0 it clicks
    def test_listen_to_clicks(self):
        safe = Safe()
        safe.rotate("R1000")
        assert safe.clicks == 10

    def test_example_2(self):
        lines = EXAMPLE_TWO
        expected = 6
        actual = answer_2(lines)
        assert expected == actual

    def test_right_wrapping_clicks(self):
        safe = Safe()
        safe.rotate("R250")
        assert safe.clicks == 3

    def test_left_wrapping_clicks(self):
        safe = Safe()
        safe.rotate("L150")
        assert safe.clicks == 2

    def test_answer_2(self):
        lines = get_resource_lines(DAY)
        answer = answer_2(lines)
        print(f"\nAnswer 2 : {answer}\n")
        # expected =
        # assert expected == answer
