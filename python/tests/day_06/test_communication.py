from unittest import TestCase

from ..util import get_resource

DAY="06"

from advent.day_06.communication import *

EXAMPLE_INPUT = """\
bvwbjplbgvbhsrlpgdmjqwftvncz:5
nppdvjthqldpwncqszvftbrmjlhg:6
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg:10
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw:11
"""

class TestThing(TestCase):

    def test_example_1(self):
        lines = EXAMPLE_INPUT.splitlines()
        for line in lines:
            expected = int(line.split(':')[1])
            line = line.split(':')[0]
            actual = answer_1(line)
            self.assertEqual(expected, actual)

    # def test_example_2(self):
    #     lines = EXAMPLE_INPUT.splitlines()
    #     expected =
    #     actual = answer_2(lines)
    #     self.assertEqual(expected, actual)

    def test_answer_1(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text()# .splitlines()
        answer = answer_1(lines)
        print(f'\nAnswer 1 : {answer}\n')
        # expected =
        # self.assertEqual(expected, answer)

    def test_answer_2(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text()# .splitlines()
        answer = answer_2(lines)
        print(f'\nAnswer 2 : {answer}\n')
        # expected =
        # self.assertEqual(expected, answer)

