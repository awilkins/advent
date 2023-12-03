import pytest

from ..util import get_resource_lines
DAY="02"

from advent.day_02.wrapping import *

EXAMPLE_ONE = """\
2x3x4
1x1x10
""".splitlines()

class TestPartOne:
    pass

    def test_parse_parcel(self):
        p = Parcel(EXAMPLE_ONE[0])
        assert p.l == 2
        assert p.w == 3
        assert p.h == 4


    @pytest.mark.parametrize('line,paper', [
        (EXAMPLE_ONE[0], 58),
        (EXAMPLE_ONE[1], 43),
    ])
    def test_areas(self, line, paper):
        p = Parcel(line)
        assert p.paper_area() == paper

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines)
        print(f'\nAnswer 1 : {answer}\n')
        # expected =
        # assert expected == answer


EXAMPLE_TWO = EXAMPLE_ONE

class TestPartTwo:
    pass

    @pytest.mark.parametrize('line,ribbon', [
        (EXAMPLE_ONE[0], 34),
        (EXAMPLE_ONE[1], 14),
    ])
    def test_example_2(self, line, ribbon):
        parcel = Parcel(line)
        assert parcel.ribbon_length() == ribbon

    def test_answer_2(self):
        lines = get_resource_lines(DAY)
        answer = answer_2(lines)
        print(f'\nAnswer 2 : {answer}\n')
        # expected =
        # assert expected == answer

