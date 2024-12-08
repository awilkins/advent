import pytest

from ..util import get_resource_lines


from advent.day_08.antenna import (
    Coord,
    Map,
    answer_1,
    answer_2,
    generate_antinode,
    generate_harmonic_antinodes,
)

DAY = "08"

EXAMPLE_ONE = """\
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
""".splitlines()

ANTINODES_1 = """\
..........
...#......
..........
....a.....
..........
.....a....
..........
......#...
..........
..........
""".splitlines()

ANTINODES_2 = """\
..........
...#......
#.........
....a.....
........a.
.....a....
..#.......
......#...
..........
..........
""".splitlines()


class TestPartOne:
    pass

    def test_generate_antinode(self):
        coords = ((4, 3), (5, 5))
        assert (3, 1) == generate_antinode(coords[0], coords[1])
        assert (6, 7) == generate_antinode(coords[1], coords[0])

    def test_parse(self):
        map = Map(ANTINODES_1)
        assert "a" == map.get_square((4, 3))
        assert {"a"} == map.get_antenna_freq()
        map_2 = Map(EXAMPLE_ONE)
        assert {"0", "A"} == map_2.get_antenna_freq()

    def test_get_antinodes(self):
        map = Map(ANTINODES_1)
        assert {(3, 1), (6, 7)} == map.get_antinodes("a")

        map_2 = Map(ANTINODES_2)
        assert {(3, 1), (0, 2), (2, 6), (6, 7)} == map_2.get_antinodes("a")

    def test_example_1(self):
        lines = EXAMPLE_ONE
        expected = 14
        actual = answer_1(lines)
        assert expected == actual

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines)
        print(f"\nAnswer 1 : {answer}\n")
        # expected =
        # assert expected == answer


EXAMPLE_TWO = EXAMPLE_ONE

ANTINODES_T = """\
T....#....
...T......
.T....#...
.........#
..#.......
..........
...#......
..........
....#.....
..........
""".splitlines()


class TestPartTwo:
    pass

    def test_harmonic_antinode_generator(self):
        one = (3, 1)
        two = (0, 0)

        expected = {(3, 1), (6, 2), (9, 3)}
        gen = generate_harmonic_antinodes(one, two, 10, 5)
        actual: set[Coord] = set(gen)
        assert expected == actual

    def test_harmonic_antinodes(self):
        map = Map(ANTINODES_T)

        expected = set()
        for yy, line in enumerate(ANTINODES_T):
            for xx, char in enumerate(line):
                if char != ".":
                    expected.add((xx, yy))
        actual = map.get_harmonic_antinodes("T")
        assert expected == actual

    def test_example_2(self):
        lines = EXAMPLE_TWO
        expected = 34
        actual = answer_2(lines)
        assert expected == actual

    def test_answer_2(self):
        lines = get_resource_lines(DAY)
        answer = answer_2(lines)
        print(f"\nAnswer 2 : {answer}\n")
        expected = 1277
        assert expected == answer
