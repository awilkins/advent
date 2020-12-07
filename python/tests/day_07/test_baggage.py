from unittest import TestCase

from ..util import get_resource

from advent.day_07.baggage import bags_in_gold, bags_of_gold

EXAMPLE_RULES = """\
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

EXAMPLE_2 = """\
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
"""

class TestBaggage(TestCase):

    def test_example_1(self):
        rules = EXAMPLE_RULES.splitlines()

        expected = 4
        actual = bags_of_gold(rules)
        self.assertEqual(expected, actual)

    def test_answer_1(self):
        rules = get_resource('day_07/input.txt').read_text().splitlines()

        answer = bags_of_gold(rules)

        # lock in answer to prevent regression
        expected = 254
        self.assertEqual(expected, answer)

        print(f'\nAnswer 1 : {answer}')

    def test_example_2(self):
        rules = EXAMPLE_2.splitlines()

        expected = 126
        actual = bags_in_gold(rules)
        self.assertEqual(expected, actual)

    def test_answer_2(self):
        rules = get_resource('day_07/input.txt').read_text().splitlines()
        answer = bags_in_gold(rules)

        expected = 6006
        self.assertEqual(expected, answer)

        print(f'\nAnswer 2 : {answer}')
