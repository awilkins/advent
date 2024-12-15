import pytest

from ..util import get_resource_lines


from advent.day_10.hiking_trails import (
    Hiker,
    Map,
    answer_1,
    answer_2,
)

DAY = "10"

NINE_TRAILS = """\
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
""".splitlines()


class TestPartOne:
    pass

    def test_map_parse(self):
        map = Map(NINE_TRAILS)
        assert 0 == map.squares[5][5]

    def test_bounds(self):
        map = Map(NINE_TRAILS)
        assert map.in_bounds((7, 7))
        assert map.in_bounds((0, 0))
        assert not map.in_bounds((-1, 0))
        assert not map.in_bounds((-1, 0))
        assert not map.in_bounds((0, -1))
        assert not map.in_bounds((7, 8))
        assert not map.in_bounds((8, 7))

    def test_next_nodes(self):
        map = Map(NINE_TRAILS)
        hiker = Hiker(map)
        hiker.current_location = (6, 4)
        assert {(6, 5)} == hiker.next_nodes()
        hiker.current_location = (4, 0)
        assert {(3, 0), (5, 0), (4, 1)} == hiker.next_nodes()

    def test_trailheads(self):
        map = Map(NINE_TRAILS)
        assert 9 == len(map.trailheads())

    def test_example_1(self):
        lines = NINE_TRAILS
        expected = 36
        actual = answer_1(lines)
        assert expected == actual

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines)
        print(f"\nAnswer 1 : {answer}\n")
        expected = 593
        assert expected == answer


EXAMPLE_TWO = NINE_TRAILS


class TestPartTwo:
    pass

    def test_example_2(self):
        lines = EXAMPLE_TWO
        expected = 81
        actual = answer_2(lines)
        assert expected == actual

    def test_answer_2(self):
        lines = get_resource_lines(DAY)
        answer = answer_2(lines)
        print(f"\nAnswer 2 : {answer}\n")
        # expected =
        # assert expected == answer
