from typing import Tuple
from unittest import TestCase

from ..util import get_resource

DAY="20"

from advent.day_20.enhance import *

EXAMPLE_INPUT = """\
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###
.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.
.#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....
.#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..
...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....
..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
"""

def process_input(lines: List[str]) -> Tuple[str, List[str]]:

    f = ""
    image_lines = None

    for line in lines:
        if len(line) and image_lines is None:
            f += line
        elif len(line) and not image_lines is None:
            image_lines.append(line)
        else:
            image_lines = []

    assert image_lines is not None
    return f, image_lines


class TestThing(TestCase):

    def test_pixlet_2_2(self):
        lines = EXAMPLE_INPUT.splitlines()
        f, image_lines = process_input(lines)
        image = Image.from_data(image_lines)
        expected = [
            [ False, False, False],
            [ True , False, False],
            [ False, True , False],
        ]
        actual = image.pixlet(2, 2)
        self.assertListEqual(expected, actual)

        f = make_filter(f)
        self.assertTrue(filtered_pixlet(actual, f))

        # print(image)
        e = image.enhanced(f)
        # print(e)
        e = e.enhanced(f)
        # print(e)

        self.assertEqual(35, len(e.pixels))

    # def test_example_2(self):
    #     lines = EXAMPLE_INPUT.splitlines()
    #     expected =
    #     actual =
    #     self.assertEqual(expected, actual)

    def test_answer_1(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
        f, i = process_input(lines)
        answer = answer_1(f, i)
        print(f'\nAnswer 1 : {answer}\n')
        self.assertLess(answer, 6564)
        self.assertGreater(answer, 5310)
        # expected =
        # self.assertEqual(expected, answer)

    # def test_answer_2(self):
    #     lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
    #     answer = answer_2(lines)
    #     print(f'\nAnswer 2 : {answer}\n')
    #     # expected =
    #     # self.assertEqual(expected, answer)

