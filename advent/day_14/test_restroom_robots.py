import pytest

from ..util import get_resource_lines


from advent.day_14.restroom_robots import (
    Robot,
    answer_1,
    answer_2,
    parse_robots,
)

DAY = "14"

EXAMPLE_ONE = """\
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
""".splitlines()


class TestPartOne:
    pass

    def test_parse_robots(self):
        robots = parse_robots(EXAMPLE_ONE)
        assert (0, 4) == robots[0].position
        assert (2, -3) == robots[10].velocity

    def test_teleporting(self):
        robot = Robot((2, 4), (2, -3))
        for _ in range(5):
            robot.move()
        assert (1, 3) == robot.position_in_bathroom((11, 7))

    def test_example_1(self):
        lines = EXAMPLE_ONE
        expected = 12
        actual = answer_1(lines, (11, 7))
        assert expected == actual

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines, (101, 103))
        print(f"\nAnswer 1 : {answer}\n")
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
        answer = answer_2(lines, (101, 103))
        print(f"\nAnswer 2 : {answer}\n")
        # expected =
        # assert expected == answer
