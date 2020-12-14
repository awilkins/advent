from unittest import TestCase

from ..util import get_resource

DAY="14"

from advent.day_14.bitcomp import *

EXAMPLE_INPUT = """\
"""

class TestThing(TestCase):


    def test_poke(self):

        comp = BitComp()

        comp.set_mask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")
        for get, put in [
            (73, 11),
            (101, 101),
            (64, 0),
        ]:
            with self.subTest(put=put):
                actual = comp.poke(8, put)
                self.assertEqual(get, actual)


    def test_splat(self):

        comp = BitComp()
        comp.set_mask("000000000000000000000000000000X1001X")

        expected = [26, 27, 58, 59]
        actual = comp.splat(42, 100)
        self.assertEqual(expected, actual)

        comp.set_mask("00000000000000000000000000000000X0XX")
        expected = [16, 17, 18, 19, 24, 25, 26, 27]
        actual = comp.splat(26, 1)
        self.assertEqual(expected, actual)

        self.assertEqual(208, comp.checksum())


    def test_answer_1(self):
        program = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        comp = BitComp()
        comp.load(program)

        answer = comp.checksum()
        print(f'\nAnswer 1 : {answer}\n')

        expected = 10050490168421
        self.assertEqual(expected, answer)


    def test_answer_2(self):
        program = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        comp = BitComp()
        comp.set_mode(2)
        comp.load(program)

        answer = comp.checksum()
        print(f'\nAnswer 2 : {answer}\n')

        expected = 2173858456958
        self.assertEqual(expected, answer)

