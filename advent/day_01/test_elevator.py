import pytest

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


@pytest.mark.parametrize('input, expected', [
    *EXAMPLES
])
def test_examples_1(input, expected):
    elevator = Elevator()
    elevator.execute(input)
    assert elevator.floor() == expected


EXAMPLES_2 = [
    (")", 1),
    ("()())", 5),
]

@pytest.mark.parametrize('input, expected', *EXAMPLES_2)
def check_2(input, expected):
    e = Elevator()
    actual = e.find_basement(input)
    assert expected == actual

class TestThing:

    def test_answer_1(self):
        line = get_resource(f'day_{DAY}/input.txt').read_text()

        answer = answer_1(line)
        print(f'\nAnswer 1 : {answer}\n')

        expected = 138
        assert expected, answer)

    def test_answer_2(self):
        line = get_resource(f'day_{DAY}/input.txt').read_text()

        answer = answer_2(line)
        print(f'\nAnswer 2 : {answer}\n')

        expected = 1771
        assert answer == expected

