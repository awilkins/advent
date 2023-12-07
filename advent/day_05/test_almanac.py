import pytest

from ..util import get_resource_lines


from advent.day_05.almanac import *

DAY = "05"

EXAMPLE_ONE = """\
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""".splitlines()


class TestPartOne:
    pass

    def test_parse(self):
        almanac = Almanac(EXAMPLE_ONE)
        assert len(almanac.seeds) == 4
        assert len(almanac.maps) == 7

    def test_mapping(self):
        al = Almanac(EXAMPLE_ONE)
        al.maps = al.maps[0:1]
        assert al.map_location(98) == 50
        assert al.map_location(99) == 51
        assert al.map_location(100) == 100
        assert al.map_location(49) == 49

    @pytest.mark.parametrize(
        "line",
        """\
seed  soil
79    81
14    14
53    55
55    57
13    13
0     0
1     1
...   ...
48    48
49    49
50    52
51    53
...   ...
96    98
97    99
98    50
99    51
""".splitlines(),
    )
    def test_multimapping(self, line: str):
        al = Almanac(EXAMPLE_ONE)
        al.maps = al.maps[0:1]
        if line[0].isdigit():
            seed, soil = [int(s) for s in line.split()]
            assert al.map_location(seed) == soil

    @pytest.mark.parametrize(
        "line",
        """\
seed  loc
79    82
14    43
55    86
13    35
""".splitlines(),
    )
    def test_loc_mapping(self, line: str):
        al = Almanac(EXAMPLE_ONE)
        if line[0].isdigit():
            seed, loc = [int(s) for s in line.split()]
            assert al.map_location(seed) == loc

    def test_example_1(self):
        lines = EXAMPLE_ONE
        expected = 35
        actual = answer_1(lines)
        assert expected == actual

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines)
        print(f"\nAnswer 1 : {answer}\n")
        expected = 403695602
        assert expected == answer


EXAMPLE_TWO = EXAMPLE_ONE


class TestPartTwo:
    pass

    def test_smallest(self):
        lines = get_resource_lines(DAY)
        al = Almanac(lines)

        smallest_destination = al.maps[-1][1][0]
        print(smallest_destination)
        smallest_source = min(map.source for map in al.maps[-1][1])
        print(smallest_source)

    def test_example_2(self):
        lines = EXAMPLE_TWO
        expected = 46
        actual = answer_2(lines)
        assert expected == actual

    @pytest.mark.skip("Very very slow")
    def test_answer_2(self):
        lines = get_resource_lines(DAY)
        answer = answer_2(lines)
        print(f"\nAnswer 2 : {answer}\n")
        expected = 219529182
        assert expected == answer

    @pytest.mark.skip("Not really implmemented")
    def test_answer_2_smart(self):
        lines = get_resource_lines(DAY)
        answer = answer_2_smart(lines)
        print(f"\nAnswer 2 : {answer}\n")
        expected = 219529182
        assert expected == answer
