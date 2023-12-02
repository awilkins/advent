import pytest

from ..util import get_resource_lines

DAY = "02"

from advent.day_02.cubes import *

EXAMPLE_ONE = """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""


class TestPartOne:
    def test_game_parser(self):
        game = Game(EXAMPLE_ONE.splitlines()[0])
        assert len(game.throws) == 3
        assert game.throws[0] == [4, 0, 3]
        assert game.throws[1] == [1, 2, 6]
        assert game.throws[2] == [0, 2, 0]

    def test_game_possible(self):
        game = Game(EXAMPLE_ONE.splitlines()[0])
        assert game.is_possible(4, 2, 6)
        assert not game.is_possible(3, 2, 6)
        assert not game.is_possible(4, 1, 6)
        assert not game.is_possible(4, 2, 5)

    def test_game_impossible(self):
        game = Game(
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
        )
        assert not game.is_possible(12, 13, 14)

    def test_example_1(self):
        lines = EXAMPLE_ONE.splitlines()
        expected = 8
        actual = answer_1(lines)
        assert expected == actual

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines)
        print(f"\nAnswer 1 : {answer}\n")
        # expected =
        # assert expected == actual


EXAMPLE_TWO = EXAMPLE_ONE


class TestPartTwo:
    @pytest.mark.parametrize(
        "game_n,expected",
        [
            (0, (4, 2, 6)),
            (1, (1, 3, 4)),
            (2, (20, 13, 6)),
            (3, (14, 3, 15)),
            (4, (6, 3, 2)),
        ],
    )
    def test_lowest_cubes(self, game_n, expected):
        game = Game(EXAMPLE_TWO.splitlines()[game_n])
        assert game.min_cubes() == expected

    def test_example_2(self):
        lines = EXAMPLE_TWO.splitlines()
        expected = 2286
        actual = answer_2(lines)
        assert expected == actual

    def test_answer_2(self):
        lines = get_resource_lines(DAY)
        answer = answer_2(lines)
        print(f'\nAnswer 2 : {answer}\n')
        # expected =
        # assert expected == actual
