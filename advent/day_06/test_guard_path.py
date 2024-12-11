import pytest

from ..util import get_resource_lines


from advent.day_06.guard_path import (
    Coord,
    DejaVuException,
    Guard,
    answer_1,
    answer_2,
    parse,
)

DAY = "06"

EXAMPL _ONE = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
""".splitlines()


class TestPartOne:
    pass

    def test_parse_input(self):
        lab, guard = parse(EXAMPLE_ONE)

        guard_position: Coord = guard.position
        assert guard_position == (4, 6)
        assert lab[9][6] == "#"

    def test_next_position(self):
        guard = Guard((2, 3), None)
        assert (2, 2) == guard.next_position()

    def test_obstruction(self):
        lab, guard_1 = parse(EXAMPLE_ONE)

        assert not guard_1.is_obstructed()

        guard_2 = Guard((4, 1), lab)
        assert guard_2.is_obstructed()

    def test_move(self):
        lab, guard_1 = parse(EXAMPLE_ONE)

        assert guard_1.position == (4, 6)
        guard_1.move()
        assert guard_1.position == (4, 5)

        guard_2 = Guard((4, 1), lab)
        guard_2.move()
        assert guard_2.position == (4, 1)  # turning to the right so in same place
        assert guard_2.facing == 1
        guard_2.move()
        assert guard_2.position == (5, 1)

    def test_guard_logging(self):
        # guard paints floor with X
        lab, guard_1 = parse(EXAMPLE_ONE)
        guard_1.move()
        assert lab[6][4] == "X"

    def test_guard_bounds_detector(self):
        lab, _ = parse(EXAMPLE_ONE)

        guard = Guard((0, 1), lab)
        guard.move()
        assert guard.is_in_bounds()
        guard.move()
        assert not guard.is_in_bounds()

    def test_example_1(self):
        lines = EXAMPLE_ONE
        expected = 41
        actual = answer_1(lines)
        assert expected == actual

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines)
        print(f"\nAnswer 1 : {answer}\n")
        expected = 4515
        assert expected == answer


EXAMPLE_TWO = EXAMPLE_ONE


class TestPartTwo:
    pass

    def test_guard_can_detect_loop(self):
        lab, guard = parse(EXAMPLE_TWO)

        lab[6][3] = "O"  # place a new obstacle
        with pytest.raises(DejaVuException):
            while guard.is_in_bounds():
                guard.move()

    def test_example_2(self):
        lines = EXAMPLE_TWO
        expected = 6
        actual = answer_2(lines)
        assert expected == actual

    def test_answer_2(self):
        lines = get_resource_lines(DAY)
        answer = answer_2(lines)
        print(f"\nAnswer 2 : {answer}\n")
        # expected =
        # assert expected == answer
