import pytest

from ..util import get_resource_lines


from advent.day_14.rolling_rocks import *

DAY="14"

EXAMPLE_ONE = """\
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
""".splitlines()

ROLLED_NORTH = """\
OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#....
""".splitlines()

ROLLED_WEST = """\
OOOO.#O...
OO..#....#
OOO..##O..
O..#OO....
........#.
..#....#.#
O....#OO..
O.........
#....###..
#....#....
""".splitlines()

class TestPartOne:
    pass

    def test_roll_north(self):
        expected = ROLLED_NORTH
        world = World(EXAMPLE_ONE)
        world.full_roll_north()
        actual = [ "".join(line) for line in world.field ]
        assert expected == actual

    def test_roll_load(self):
        expected = ROLLED_NORTH
        world = World(EXAMPLE_ONE)
        world.full_roll_north()
        assert 136 == world.load()

    def test_answer_1(self):

        lines = get_resource_lines(DAY)
        answer = answer_1(lines)
        print(f'\nAnswer 1 : {answer}\n')
        # expected =
        # assert expected == answer


EXAMPLE_TWO = EXAMPLE_ONE

CYCLE_ONE = """\
.....#....
....#...O#
...OO##...
.OO#......
.....OOO#.
.O#...O#.#
....O#....
......OOOO
#...O###..
#..OO#....
""".splitlines()

SMALL_WORLD = """\
...
.#.
..O
""".splitlines()

class TestPartTwo:
    pass
    
    def test_west(self):
        n = World(ROLLED_NORTH)
        n.full_roll_west()
        actual = [
            "".join(line) for line in n.field
        ]
        assert actual == ROLLED_WEST
    
    def test_cycle(self):
        world = World(EXAMPLE_TWO)
        world.cycle()
        actual = [
            "".join(line) for line in world.field
        ]
        assert actual == CYCLE_ONE

    def test_basic_cycle(self):
        world = World(SMALL_WORLD)
        world.cycle()
        actual = [
            "".join(line) for line in world.field
        ]
        assert actual == SMALL_WORLD

    def test_example_2(self):
        lines = EXAMPLE_TWO
        expected = 64
        actual = answer_2(lines)
        assert expected == actual

    def test_answer_2(self):
        lines = get_resource_lines(DAY)
        answer = answer_2(lines)
        print(f'\nAnswer 2 : {answer}\n')
        # expected =
        # assert expected == answer

