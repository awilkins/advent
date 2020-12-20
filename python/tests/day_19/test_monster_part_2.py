from unittest import TestCase

from tests.util import get_resource

DAY = "19"

from advent.day_19.monster import *


class TestPart2(TestCase):

    def test_example_2(self):
        rules, messages = parse_input(EXAMPLE_INPUT.splitlines())

        possibles = set(possible_messages(rules, rules[0]))
        expected = 3
        actual = sum([1 for message in messages if message in possibles])
        self.assertEqual(expected, actual)

        patch(rules)
        for m in possible_messages(rules, rules[11]):
            print(m)

    def test_answer_2(self):
        input_lines =get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        rules, messages = parse_input(input_lines)
        patch(rules)

        messages = list([(len(m), m) for m in messages])
        messages.sort()


        count = 0
        bad = set([])
        for _, m in messages:
            for b in bad:
                thisbad = False
                if m[:len(b)] == b:
                    print("skipbad!")
                    thisbad = True
                    break
                if thisbad == True: continue

            for p in possible_messages(rules, rules[0]):
                if len(p) > len(m):
                    print(f"bad : {m}")
                    bad.add(m)
                    break
                if p == m:
                    count += 1
                    print(f"gud : {m}")
                    break

        print(f"\nAnswer 2: {count}")


EXAMPLE_INPUT = """\
42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
"""

if "__main__" == __name__:
    test = TestPart2()
    test.test_answer_2()
