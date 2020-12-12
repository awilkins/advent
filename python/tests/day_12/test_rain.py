from advent.day_12.rain import Ship
from unittest import TestCase

from ..util import get_resource

DAY="12"

from advent.day_12.rain import *

EXAMPLE_INPUT = """\
F10
N3
F7
R90
F11
"""

class TestThing(TestCase):


    def test_example_1(self):
        input_lines = EXAMPLE_INPUT.splitlines()

        expected = 25

        ship = Ship()
        ship.navigate(input_lines)
        actual = ship.manhattan_distance()

        self.assertEqual(expected, actual)


    def test_answer_1(self):
        input_lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        expected = 582
        ship = Ship()
        ship.navigate(input_lines)
        answer = ship.manhattan_distance()
        self.assertEqual(expected, answer)
        print(f'\nAnswer 1 : {answer}\n')


    def test_rotation(self):
        ship = Ship(2, 1)

        ship.rotate("R", 90)
        self.assertEqual(1, ship.x)
        self.assertEqual(-2, ship.y)

        ship.rotate("L", 90)
        self.assertEqual(2, ship.x)
        self.assertEqual(1, ship.y)



    def test_example_2(self):
        input_lines = EXAMPLE_INPUT.splitlines()

        expected = 286

        ship = Ship()
        ship.navigate_by_waypoint([input_lines[0]])
        self.assertEqual(100, ship.x)
        self.assertEqual(10, ship.y)

        ship.navigate_by_waypoint([input_lines[1]])
        self.assertEqual(10, ship.waypoint.x)
        self.assertEqual(4, ship.waypoint.y)

        ship.navigate_by_waypoint([input_lines[2]])
        self.assertEqual(170, ship.x)
        self.assertEqual(38, ship.y)

        ship.navigate_by_waypoint([input_lines[3]])
        self.assertEqual(4, ship.waypoint.x)
        self.assertEqual(-10, ship.waypoint.y)

        ship.navigate_by_waypoint([input_lines[4]])
        self.assertEqual(214, ship.x)
        self.assertEqual(-72, ship.y)

        actual = ship.manhattan_distance()
        self.assertEqual(expected, actual)

    def test_answer_2(self):
        input_lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        expected = 52069
        ship = Ship()
        ship.navigate_by_waypoint(input_lines)
        answer = ship.manhattan_distance()
        self.assertEqual(expected, answer)
        print(f'\nAnswer 2 : {answer}\n')
