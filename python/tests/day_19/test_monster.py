from unittest import TestCase
from unittest.case import skip

from tests.util import get_resource

DAY="19"

from advent.day_19.monster import *

EXAMPLE_INPUT = """\
0: 1 2
1: "a"
2: 1 3 | 3 1
3: "b"

a
b
ab
ba
aab
aba
"""

EXAMPLE_TWO = """\
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

a
"""

class TestThing(TestCase):

    def test_integer_message(self):
        BIG_MESS = "babaaaaaabaabaaaaaababbaaaabbabbbaababbbaaabbabbaaabbabbaaaabaabbaabbbababbaabaaababbaab"
        print(convert_to_int(BIG_MESS))


    def test_example_1(self):
        input_lines = EXAMPLE_INPUT.splitlines()

        rules, messages = parse_input(input_lines)

        self.assertEqual(6, len(messages))
        self.assertEqual(4, len(rules))

        possibles = list(possible_messages(rules, rules[1]))
        self.assertListEqual(['a'], possibles)

        possibles = list(possible_messages(rules, rules[2]))
        self.assertListEqual(
            ['ab', 'ba'],
            possibles,
        )

        possibles = list(possible_messages(rules, rules[0]))
        for m in possibles:
            print(m)

        self.assertListEqual(
            ['aab', 'aba'],
            possibles,
        )


    def test_example_two(self):
        lines = EXAMPLE_TWO.splitlines()

        rules, _ = parse_input(lines)
        expected = [
            "aaaabb",
            "aaabab",
            "abbabb",
            "abbbab",
            "aabaab",
            "aabbbb",
            "abaaab",
            "ababbb"
        ]

        actual = list(possible_messages(rules, rules[0]))
        self.assertListEqual(expected, actual)


# @skip('too slow')
def test_answer_1(self):
        input_lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        rules, messages = parse_input(input_lines)

        possibles = set(possible_messages(rules, rules[0]))

        answer = sum(1 for message in messages if message in possibles)

        print(f'\nAnswer 1 : {answer}\n')

        expected = 195
        self.assertEqual(expected, answer)

    # def test_answer_2(self):
    #     input_lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

    #     answer =
    #     print(f'\nAnswer 2 : {answer}\n')

    #     # expected =
    #     # self.assertEqual(expected, answer)

