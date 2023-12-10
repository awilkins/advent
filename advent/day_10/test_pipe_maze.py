import pytest

from ..util import get_resource_lines


from advent.day_10.pipe_maze import *

DAY = "10"

EXAMPLE_ONE = """\
.....
.S-7.
.|.|.
.L-J.
.....
""".splitlines()

MESSED_UP = """\
-L|F7
7S-7|
L|7||
-L-J|
L|-JF
""".splitlines()


class TestPartOne:
    pass

    def test_parse(self):
        maze = Maze(EXAMPLE_ONE)
        assert len(maze.squares) == 5

    def test_get_start(self):
        maze = Maze(EXAMPLE_ONE)
        assert (1, 1) == maze.get_start()

    def test_get_loop(self):
        maze = Maze(EXAMPLE_ONE)
        assert (1, 2) == maze.find_loop_around_start()

    @pytest.mark.parametrize(
        "lines",
        [
            EXAMPLE_ONE,
            MESSED_UP,
        ],
    )
    def test_navigate_loop(self, lines):
        maze = Maze(lines)
        path = list(maze.navigate_loop())

        assert [
            (1, 1),
            (1, 2),
            (1, 3),
            (2, 3),
            (3, 3),
            (3, 2),
            (3, 1),
            (2, 1),
        ] == path

    def test_example_1(self):
        lines = EXAMPLE_ONE
        expected = 4
        actual = answer_1(lines)
        assert expected == actual

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines)
        print(f"\nAnswer 1 : {answer}\n")
        # expected =
        # assert expected == answer


EXAMPLE_TWO = """\
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
""".splitlines()

EXAMPLE_THREE = """\
..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
..........
""".splitlines()



class TestPartTwo:
    pass

    def test_example_2(self):
        lines = EXAMPLE_TWO
        expected = 4
        actual = answer_2(lines)
        assert expected == actual

    def test_example_3(self):
        lines = EXAMPLE_THREE
        expected = 4
        actual = answer_2(lines)
        assert expected == actual

    def test_answer_2(self):
        lines = get_resource_lines(DAY)
        answer = answer_2(lines)
        print(f'\nAnswer 2 : {answer}\n')
        # expected =
        # assert expected == answer
