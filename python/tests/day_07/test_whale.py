from unittest import TestCase

from ..util import get_resource

DAY="07"

from advent.day_07.whale import *

EXAMPLE_INPUT = """\
16,1,2,0,4,2,7,1,2,14
"""

SUBS = [ int(s) for s in EXAMPLE_INPUT.split(',') ]

class TestThing(TestCase):

    def test_fuel_cost(self):

        expected = 37
        actual = fuel_cost(SUBS, 2)

        self.assertEqual(expected, actual)

    def test_find(self):
        self.assertEqual((2, 37), find_cheapest(SUBS))

    def test_answer_1(self):
        subs = [
            int(s) for s in
            get_resource(f'day_{DAY}/input.txt').read_text().split(',')
        ]

        position, answer = find_cheapest(subs)
        print(f'\nAnswer 1 : {answer}\n')

        self.assertEqual(383, position)
        expected = 352254
        self.assertEqual(expected, answer)


    def test_move_cost(self):
        self.assertEqual(66, move_cost(16, 5))
        self.assertEqual(10, move_cost(1, 5))


    def test_real_cost(self):
        self.assertEqual(168, real_fuel_cost(SUBS, 5))
        self.assertEqual(206, real_fuel_cost(SUBS, 2))

    def test_answer_2(self):
        subs = [
            int(s) for s in
            get_resource(f'day_{DAY}/input.txt').read_text().split(',')
        ]

        position, answer = find_cheapest(subs, real_fuel_cost)
        print(f'\nAnswer 2 : {position}, {answer}\n')

        self.assertEqual(504, position)
        expected = 99053143
        self.assertEqual(expected, answer)
