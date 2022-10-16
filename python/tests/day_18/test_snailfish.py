from unittest import TestCase

from ..util import get_resource

DAY="18"

from advent.day_18.snailfish import *

EXAMPLE_1 = """\
[1,2]
[[1,2],3]
[9,[8,7]]
[[1,9],[8,5]]
[[[[1,2],[3,4]],[[5,6],[7,8]]],9]
[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]
[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]
"""

class TestThing(TestCase):

    def test_parse_and_string(self):
        lines = EXAMPLE_1.splitlines()
        for line in lines:
            actual = str(Pair.parse(line))
            self.assertEqual(line, actual)

    # def test_example_2(self):
    #     lines = EXAMPLE_INPUT.splitlines()
    #     expected =
    #     actual =
    #     self.assertEqual(expected, actual)

    # def test_answer_1(self):
    #     lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
    #     answer = answer_1(lines)
    #     print(f'\nAnswer 1 : {answer}\n')
    #     # expected =
    #     # self.assertEqual(expected, answer)

    # def test_answer_2(self):
    #     lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
    #     answer = answer_2(lines)
    #     print(f'\nAnswer 2 : {answer}\n')
    #     # expected =
    #     # self.assertEqual(expected, answer)

