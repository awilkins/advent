from unittest import TestCase

from ..util import get_resource

DAY="08"

from advent.day_08.segmented import *

EXAMPLE_INPUT = """\
acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
"""

MORE_EXAMPLES = """\
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""

class TestThing(TestCase):

    def test_example_1(self):
        lines = MORE_EXAMPLES.splitlines()

        expected = 26
        actual = count_unique(lines)

        self.assertEqual(expected, actual)

    def test_answer_1(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        answer = count_unique(lines)
        print(f'\nAnswer 1 : {answer}\n')

        # expected =
        # self.assertEqual(expected, answer)


    def test_signal_map(self):
        digits = EXAMPLE_INPUT.split("|")[0].strip().split()
        answer = deduce_signal_map(digits)
        expected = [
            'cagedb',
            'ab',
            'gcdfa',
            'fbcad',
            'eafb',
            'cdfbe',
            'cdfgeb',
            'dab',
            'acedgfb',
            'cefabd',
        ]
        expected = [ ''.join(sorted(n)) for n in expected ]
        self.assertListEqual(expected, answer)


    def test_answer_2(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        answer = sum([ get_value(line) for line in lines ])
        print(f'\nAnswer 2 : {answer}\n')

        # expected =
        # self.assertEqual(expected, answer)

