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
""".splitlines()


class TestPartOne:
    pass

    @pytest.mark.parametrize(
        "throw,expected",
        [
            ("3 red, 5 green, 4 blue", (3, 5, 4)),
            ("4 red, 6 green, 3 blue", (4, 6, 3)),
            ("3 blue, 4 red", (4, 0, 3)),
        ],
    )
    def test_cube_counts(self, throw, expected):
        assert parse_throw(throw) == expected

    def test_parse_game(self):
        input = "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        expected = [
            (4, 0, 3),
            (1, 2, 6),
            (0, 2, 0),
        ]
        assert parse_game(input) == expected

    def test_game_constructor(self):
        input = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        expected = [
            (4, 0, 3),
            (1, 2, 6),
            (0, 2, 0),
        ]
        game = Game(input)
        assert game.throws == expected
        assert game.id == 1

    def test_game_is_possible(self):
        input = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        game = Game(input)
        assert game.is_possible(4, 2, 6)

    def test_game_is_impossible(self):
        input = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        game = Game(input)
        assert not game.is_possible(3, 2, 6)
        assert not game.is_possible(4, 1, 6)
        assert not game.is_possible(4, 2, 5)

    def test_example_1(self):
        lines = EXAMPLE_ONE
        expected = 8
        actual = answer_1(lines)
        assert expected == actual

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines)
        print(f"\nAnswer 1 : {answer}\n")
        expected = 2006
        assert expected == answer


EXAMPLE_TWO = EXAMPLE_ONE


class TestPartTwo:
    pass

    @pytest.mark.parametrize(
        "line,expected",
        [
            (EXAMPLE_TWO[0], (4, 2, 6)),
            (EXAMPLE_TWO[1], (1, 3, 4)),
            (EXAMPLE_TWO[2], (20, 13, 6)),
            (EXAMPLE_TWO[3], (14, 3, 15)),
            (EXAMPLE_TWO[4], (6, 3, 2)),
        ],
    )
    def test_minimum_cubes(self, line, expected):
        game = Game(line)
        assert game.min() == expected

    def test_example_2(self):
        lines = EXAMPLE_TWO
        expected = 2286
        actual = answer_2(lines)
        assert expected == actual

    def test_answer_2(self):
        lines = get_resource_lines(DAY)
        answer = answer_2(lines)
        print(f'\nAnswer 2 : {answer}\n')
        expected = 84911
        assert expected == answer
