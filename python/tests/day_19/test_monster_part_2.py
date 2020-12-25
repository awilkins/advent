from os import pathconf
from unittest import TestCase

import re

from tests.util import get_resource

DAY = "19"

from advent.day_19.monster import *


class TestPart2(TestCase):
    
    def test_valid_regex(self):
        rules, _ = parse_input(EXAMPLE_INPUT.splitlines())
        
        reggie = convert_rules_to_regex(rules)
        re.compile(reggie)
        
        patch(rules)
        reg2 = convert_rules_to_regex(rules)
        re.compile(reg2)

        # Didn't crash? Great!
    
    
    def test_part_1(self):
        input_lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
        rules, messages = parse_input(input_lines)
        
        reg = convert_rules_to_regex(rules)
        rec = re.compile(reg)

        count = 0
        for m in messages:
            if rec.match(m):
                count += 1
        
        self.assertEqual(195, count)
        

    def test_part_2(self):
        input_lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
        rules, messages = parse_input(input_lines)

        patch(rules)

        reg = convert_rules_to_regex(rules)
        print(reg)
        rec = re.compile(reg)

        count = 0
        for m in messages:
            if rec.match(m):
                count += 1
        
        print(f"\nAnswer 2: {count}")
        assert count < 319
        assert count > 259
        assert count != 6
        assert count == 309
        # self.assertEqual(195, count)
        

EXAMPLE_INPUT_1 = """\
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
