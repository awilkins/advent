from unittest import TestCase

from ..util import get_resource

DAY="01"

from advent.day_01.elevator import *

EXAMPLES = [
    ("(())", 0),
    ("()()", 0),
    ("(((", 3),
    ("(()(()(", 3),
    ("))(((((", 3),
    ("())", -1),
    ("))(", -1),
    (")))", -3),
    (")())())", -3),
]

def check(input, expected):
    elevator = Elevator()
    elevator.execute(input)
    assert elevator.floor() == expected

def test_examples_1():
    for input, expected in EXAMPLES:
        yield check, input, expected


def check_2(input, expected):
    e = Elevator()
    actual = e.find_basement(input)
    assert expected == actual

EXAMPLES_2 = [
    (")", 1),
    ("()())", 5),
]

def test_examples_2():
    for input, expected in EXAMPLES_2:
        yield check_2, input, expected


class TestThing(TestCase):


    def test_answer_1(self):
        line = get_resource(f'day_{DAY}/input.txt').read_text()

        answer = answer_1(line)
        print(f'\nAnswer 1 : {answer}\n')

        # expected =
        # self.assertEqual(expected, answer)

    def test_answer_2(self):
        line = get_resource(f'day_{DAY}/input.txt').read_text()

        answer = answer_2(line)
        print(f'\nAnswer 2 : {answer}\n')

    #     # expected =
    #     # self.assertEqual(expected, answer)

