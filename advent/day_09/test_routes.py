import pytest

from ..util import get_resource_lines


from advent.day_09.routes import *

DAY = "09"

EXAMPLE_ONE = """\
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
""".splitlines()


class TestPartOne:
    pass

    def test_parse(self):
        route = Route("Maghull to York = 12")
        assert route.start == "Maghull"
        assert route.dest == "York"
        assert route.distance == 12

    def test_example_1(self):
        lines = EXAMPLE_ONE
        expected = 605
        actual = answer_1(lines)
        assert expected == actual

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines)
        print(f'\nAnswer 1 : {answer}\n')
        # expected =
        # assert expected == answer


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
        answer = answer_2(lines)
        print(f'\nAnswer 2 : {answer}\n')
        # expected =
        # assert expected == answer
