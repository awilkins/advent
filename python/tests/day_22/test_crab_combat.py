from unittest import TestCase

from pathlib import Path
from unittest.case import skip
from ..util import get_resource

DAY="22"

from advent.day_22.crab_combat import *

EXAMPLE_INPUT = """\
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
"""

INFINITE_GAME = """\
Player 1:
43
19

Player 2:
2
29
14
"""

class TestThing(TestCase):

    def test_example_1(self):
        lines = EXAMPLE_INPUT.splitlines()

        expected = 306
        actual = play_combat(lines)

        self.assertEqual(expected, actual)

    def test_answer_1(self):
        input_lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        answer = play_combat(input_lines)
        print(f'\nAnswer 1 : {answer}\n')

        expected = 32033
        self.assertEqual(expected, answer)


    def test_no_recursion(self):
        lines = INFINITE_GAME.splitlines()

        score = play_recursive_combat(lines)
        for line in log:
            print(line)


    @skip("Takes too long")
    def test_example_2(self):
        lines = EXAMPLE_INPUT.splitlines()
        score, game = play_recursive_combat(lines)

        self.assertEqual(291, score)
        self.assertListEqual(
            [7, 5, 6, 2, 4, 1, 10, 8, 9, 3],
            list(game.player2)
        )

        sample_log = get_resource(f'day_{DAY}/example_game_log.txt').read_text().splitlines()
        self.assertListEqual(sample_log, log)


    def test_answer_2(self):
        input_lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        answer, game = play_recursive_combat(input_lines)
        print(f'\nAnswer 2 : {answer}\n')
        print(game.player1)
        print(game.player2)

        with Path('/tmp/log.txt').open('w') as file:
            for line in log:
                file.write(line)
                file.write("\n")

        assert 34746 < answer
        # expected =
        # self.assertEqual(expected, answer)

