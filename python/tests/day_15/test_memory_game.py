from unittest import TestCase
from unittest.case import skip


from ..util import get_resource

DAY="15"

from advent.day_15.memory_game import *


class TestMemory(TestCase):


    def test_example_1(self):
        numbers = "0,3,6"

        expected = 436
        actual = play(numbers)

        self.assertEqual(expected, actual)


    def test_answer_1(self):
        input_lines = "2,0,1,9,5,19"

        answer = play(input_lines)
        print(f'\nAnswer 1 : {answer}\n')

        expected = 1009
        self.assertEqual(expected, answer)


    # def test_next(self):

    #     numbers = [0, 3, 6, 0, 3, 3, 1, 0, 4, 0]

    #     ii = 0
    #     next_list = next_number(numbers[0:3])
    #     for n in next_list:
    #         self.assertEqual(n, numbers[ii], f"ii = {ii}")
    #         ii += 1
    #         if ii >= len(numbers): break


    @skip("way too slow")
    def test_part_2(self):
        tests = [
            ("0,3,6", 175594),
            ("1,3,2", 2578),
            ("2,1,3", 3544142),
            ("1,2,3", 261214),
            ("2,3,1", 6895259),
            ("3,2,1", 18),
            ("3,1,2", 362),
        ]

        for numbers, expected in tests:
            with self.subTest(numbers=numbers, expected=expected):
                actual = play(numbers, 30_000_000)
                self.assertEqual(expected, actual)

    # def test_answer_2(self):
    #     input_lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

    #     answer =
    #     print(f'\nAnswer 2 : {answer}\n')

    #     # expected =
    #     # self.assertEqual(expected, answer)

