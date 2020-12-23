from unittest import TestCase

from ..util import get_resource

DAY="23"

from advent.day_23.crab_cups import *

EXAMPLE_INPUT = "389125467"

ACTUAL_INPUT = "586439172"

class TestThing(TestCase):

    def test_example_1(self):
        line = EXAMPLE_INPUT

        expected = "92658374"
        actual = play(line, 10)

        self.assertEqual(expected, actual)

    def test_answer_1(self):
        line = ACTUAL_INPUT

        answer = play(line)
        print(f'\nAnswer 1 : {answer}\n')

        expected = "28946753"
        self.assertEqual(expected, answer)

    def test_example_2(self):
        line = EXAMPLE_INPUT

        expected = "92658374"
        actual = play2(line)

        self.assertEqual(expected, actual)


    def test_example_1_play_2(self):
        line = EXAMPLE_INPUT
        expected = "92658374"

        circle = Circle([int(c) for c in line])

        count = 0
        while count < 10:
            circle.move()
            count += 1

        out = []
        next_cup = circle.one_cup.next
        for ii in range(8):
            out.append(next_cup)
            next_cup = next_cup.next

        actual = "".join(str(cup.value) for cup in out)
        self.assertEqual(expected, actual)



    # def test_answer_2(self):
    #     lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

    #     answer =
    #     print(f'\nAnswer 2 : {answer}\n')

    #     # expected =
    #     # self.assertEqual(expected, answer)

