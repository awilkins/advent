import pytest

from ..util import get_resource_lines


from advent.day_17.crucible import *

DAY = "17"

EXAMPLE_ONE = """\
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
""".splitlines()


class TestPartOne:
    pass

    @pytest.mark.parametrize('vec', DIRECTIONS)
    def test_path_does_not_double_back(self, vec: Vector):

        possible = next_paths(
            vec, 1
        )
        assert vec.opposite() not in [v for v, i in possible]

    @pytest.mark.parametrize('vec', DIRECTIONS)
    def test_path_continues_after_2(self, vec: Vector):

        possible = next_paths(
            vec, 1
        )
        assert vec in [v for v, i in possible]

    @pytest.mark.parametrize('vec', DIRECTIONS)
    def test_path_turns_after_3(self, vec: Vector):

        possible = next_paths(
            vec, 2
        )
        assert vec not in [v for v, i in possible]


    def test_example_1(self):
        lines = EXAMPLE_ONE
        expected = 102
        actual = answer_1(lines)
        assert expected == actual

    # @pytest.mark.skip('Slow')
    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines)
        print(f'\nAnswer 1 : {answer}\n')
        assert answer > 893
        expected = 902
        assert expected == answer


EXAMPLE_TWO = EXAMPLE_ONE


class TestPartTwo:
    pass

    def test_example_2(self):
        lines = EXAMPLE_TWO
        expected = 94
        actual = answer_2(lines)
        assert expected == actual

    # @pytest.mark.skip('Slow')
    def test_answer_2(self):
        lines = get_resource_lines(DAY)
        answer = answer_2(lines)
        print(f'\nAnswer 2 : {answer}\n')
        expected = 1073
        assert expected == answer
