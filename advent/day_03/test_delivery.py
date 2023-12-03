import pytest

from ..util import get_resource_lines
DAY="03"

from advent.day_03.delivery import *

EXAMPLE_ONE = """\
>
^>v<
^v^v^v^v^v
""".splitlines()

class TestPartOne:
    pass

    def test_east(self):
        world = World()
        traveller = Traveller(world)
        assert world.delivered_squares() == 1
        traveller.deliver(EAST)
        assert world.delivered_squares() == 2
        assert world.x_offset == 0
        assert world.world == deque([
            deque([1, 1])
        ])


    def test_one(self):
        line = EXAMPLE_ONE[0]
        assert 2 == answer_1(line)

    def test_two(self):
        line = EXAMPLE_ONE[1]
        assert 4 == answer_1(line)

    def test_three(self):
        line = EXAMPLE_ONE[2]
        assert 2 == answer_1(line)

    # def test_example_1(self):
    #     lines = EXAMPLE_ONE
    #     expected =
    #     actual = answer_1(lines)
    #     assert expected == actual

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines[0])
        print(f'\nAnswer 1 : {answer}\n')
        expected = 2592
        assert expected == answer


EXAMPLE_TWO = EXAMPLE_ONE

class TestPartTwo:
    pass

    # def test_example_2(self):
    #     lines = EXAMPLE_TWO
    #     expected =
    #     actual = answer_2(lines)
    #     assert expected == actual

    def test_answer_2(self):
        lines = get_resource_lines(DAY)
        answer = answer_2(lines[0])
        print(f'\nAnswer 2 : {answer}\n')
        # expected =
        # assert expected == answer

