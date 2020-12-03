from unittest import TestCase

from ..util import get_resource

from advent.day_03.toboggan import multi_traverse, traverse_trees

EXAMPLE_INPUT = '''\
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#\
'''

class TobogganTest(TestCase):

    def test_example(self):

        self.assertEqual(7, traverse_trees(EXAMPLE_INPUT.split('\n')))

    def test_answer_1(self):
        map_lines = get_resource('day_03/input.txt').open().readlines()
        print(f'Answer 1 : {traverse_trees(map_lines)}')

    def test_answer_2(self):
        map_lines = get_resource('day_03/input.txt').open().readlines()
        slopes = [
            (1, 1),
            (3, 1),
            (5, 1),
            (7, 1),
            (1, 2),
        ]
        print(f'Answer 2 : {multi_traverse(map_lines, slopes)}')

