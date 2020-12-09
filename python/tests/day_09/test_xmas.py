from unittest import TestCase

from ..util import get_resource

from advent.day_09.xmas import *

EXAMPLE_5 = """\
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
"""

class TestXmas(TestCase):

    def test_25(self):
        xmas = list([str(r) for r in range(1, 26)])

        for t, r in [
            (26, True),
            (49, True),
            (100, False),
            (50, False),
        ]:
            xmas_input = xmas.copy()
            xmas_input.append(t)
            actual = find_xmas_flaw(xmas_input, 25)
            if r:
                expected = -1
            else:
                expected = t
            self.assertEqual(expected, actual)

    def test_5(self):
        xmas = EXAMPLE_5.splitlines()

        expected = 127
        actual = find_xmas_flaw(xmas, 5)
        self.assertEqual(expected, actual)

        expected = 62
        actual = find_xmas_weakness(xmas, actual)
        self.assertEqual(expected, actual)

    def test_answer(self):
        xmas = get_resource('day_09/input.txt').read_text().splitlines()

        answer = find_xmas_flaw(xmas, 25)
        self.assertEqual(1639024365, answer)
        print(f'\nAnswer 1 : {answer}')

        answer = find_xmas_weakness(xmas, answer)
        self.assertEqual(219202240, answer)
        print(f'\nAnswer 2 : {answer}')
