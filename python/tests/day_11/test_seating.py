from unittest import TestCase, skip

from ..util import get_resource

DAY="11"

from advent.day_11.seating import *

EXAMPLE_INPUT = """\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""

ONE = """\
L#L
LLL
LLL
"""

#   x------>
#  y 0 1 2
#  |0
#  |1
#  |2
#  v

class TestSeating(TestCase):

    def test_adjacent_count(self):
        input_lines = parse_input(ONE.splitlines())

        ones = [
            (0, 0),
            (2, 0),
            (0, 1),
            (1, 1),
            (2, 1),
        ]
        expected = 1
        for x, y in ones:
            actual = adjacent_count(input_lines, x, y)
            self.assertEqual(expected, actual)

        zeroes = [
            (0, 2),
            (1, 2),
            (2, 2),
        ]
        expected = 0
        for x, y in zeroes:
            actual = adjacent_count(input_lines, x, y)
            self.assertEqual(expected, actual)

    def test_seat_count(self):
        grid = SeatGrid(ONE.splitlines())

        expected = 1
        actual = grid.count_occupied()
        self.assertEqual(expected, actual)


    def test_example_1(self):
        input_lines = EXAMPLE_INPUT.splitlines()

        grid = SeatGrid(input_lines)
        grid.settle()

        expected = 37
        count = grid.count_occupied()

        self.assertEqual(expected, count)

    @skip("takes too long")
    def test_answer_1(self):
        input_lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        grid = SeatGrid(input_lines)
        grid.settle()

        answer = grid.count_occupied()

        expected = 2310
        self.assertEqual(expected, answer)
        print(f'\nAnswer 1 : {answer}\n')


    def test_visible_count(self):
        input_lines = parse_input(ONE.splitlines())

        ones = [
            (2, 0),
            (0, 0),
            (0, 1),
            (1, 1),
            (2, 1),
        ]
        expected = 1
        for x, y in ones:
            actual = visible_count(input_lines, x, y)
            self.assertEqual(expected, actual)

        zeroes = [
            (1, 0),
            (0, 2),
            (1, 2),
            (2, 2),
        ]
        expected = 0
        for x, y in zeroes:
            actual = visible_count(input_lines, x, y)
            self.assertEqual(expected, actual)

    def test_eight_visible_seats(self):
        input_lines = """\
.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....
""".splitlines()

        expected = 8
        actual = visible_count(input_lines, 3, 4)
        self.assertEqual(expected, actual)

    def test_no_visible_full_seats(self):
        input_lines = """\
.............
.L.L.#.#.#.#.
.............
""".splitlines()

        expected = 0
        actual = visible_count(input_lines, 1, 1)
        self.assertEqual(expected, actual)

    def test_no_visible_seats(self):
        input_lines = """\
.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.
""".splitlines()

        expected = 0
        actual = visible_count(input_lines, 3, 3)
        self.assertEqual(expected, actual)

    def test_example_2(self):
        input_lines = EXAMPLE_INPUT.splitlines()
        grid = SeatGrid(input_lines)
        grid.visibility = visible_count
        grid.occupancy_threshold = 5
        grid.settle(True)

        expected = 26
        actual = grid.count_occupied()
        self.assertEqual(expected, actual)


    @skip('Takes too long')
    def test_answer_2(self):
        input_lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        grid = SeatGrid(input_lines)
        grid.visibility = visible_count
        grid.occupancy_threshold = 5
        grid.settle()

        answer = grid.count_occupied()

        expected = 2074
        self.assertEqual(expected, answer)
        print(f'\nAnswer 2 : {answer}\n')
