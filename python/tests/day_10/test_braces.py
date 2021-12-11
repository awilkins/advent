from unittest import TestCase

from ..util import get_resource

DAY="10"

from advent.day_10.braces import *

EXAMPLE_1 = """\
{([(<{}[<>[]}>{[]{[(<()>
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
"""

EXAMPLE_INPUT = """\
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""

class TestThing(TestCase):

    def test_validation(self):
        lines = EXAMPLE_1.splitlines()

        self.assertEqual((False, "}"), validate_line(lines[0]))
        self.assertEqual((False, ")"), validate_line(lines[1]))
        self.assertEqual((False, "]"), validate_line(lines[2]))
        self.assertEqual((False, ")"), validate_line(lines[3]))
        self.assertEqual((False, ">"), validate_line(lines[4]))

        self.assertEqual((True, ""), validate_line(
            "https://meet.google.com/aqb-xuqx-iuf"))

    def test_example_1(self):
        lines = EXAMPLE_INPUT.splitlines()

        expected = 26397
        actual = answer_1(lines)

        self.assertEqual(expected, actual)

    def test_answer_1(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        answer = answer_1(lines)
        print(f'\nAnswer 1 : {answer}\n')

        expected = 462693
        self.assertEqual(expected, answer)

    def test_completion(self):

        TESTS = [
            ("[({(<(())[]>[[{[]{<()<>>", "}}]])})]"),
            ("[(()[<>])]({[<{<<[]>>(", ")}>]})"),
            ("(((({<>}<{<{<>}{[]{[]{}", "}}>}>))))"),
            ("{<[[]]>}<{[{[{[]{()[[[]", "]]}}]}]}>"),
            ("<{([{{}}[<[[[<>{}]]]>[]]", "])}>"),
        ]

        for input, expected in TESTS:
            self.assertEqual(expected, complete_line(input))


    def test_score(self):
        self.assertEqual(294, score_completion("])}>"))


    def test_answer_2(self):
        lines = EXAMPLE_INPUT.splitlines()

        self.assertEqual(288957, answer_2(lines))

        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
        answer = answer_2(lines)
        print(f'\nAnswer 2 : {answer}\n')

        # expected =
        # self.assertEqual(expected, answer)

