from datetime import time
from unittest import TestCase
from unittest.case import skip

from ..util import get_resource

DAY="13"

from advent.day_13.buses import *

EXAMPLE_INPUT = """\
939
7,13,x,x,59,x,31,19
"""

class TestThing(TestCase):



    # def test_example_1(self):
    #     input_lines = EXAMPLE_INPUT.splitlines()

    #     expected =
    #     actual =

    #     self.assertEqual(expected, actual)

    def test_answer_1(self):
        input_lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        expected = 5946
        answer = time_1(input_lines)
        self.assertEqual(expected, answer)
        print(f'\nAnswer 1 : {answer}\n')

    @skip("asefwef")
    def test_example_1(self):
        for lines, expected in [
            (["", "17,x,13,19"], 3417),
            (EXAMPLE_INPUT.splitlines(), 1068781),
            (["", "67,7,59,61"], 754018),
            (["", "67,x,7,59,61"], 779210),
            (["", "67,7,x,59,61"], 1261476),
            (["", "1789,37,47,1889"], 1202161486),
        ]:
            with self.subTest(line=lines[1]):
                self.assertEqual(expected, time_2(lines))

        # lines = EXAMPLE_INPUT.splitlines()
        # expected = 1068781

        # answer = time_2(lines)
        # self.assertEqual(expected, answer)

    # @skip("bkasodf")
    def test_answer_2(self):
        input_lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        # expected =
        answer = time_2(input_lines)
        # self.assertEqual(expected, answer)
        print(f'\nAnswer 2 : {answer}\n')

