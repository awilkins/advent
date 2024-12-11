from advent.day_05.printqueue import (
    answer_1,
    answer_2,
    is_ordered,
    middle_num,
    parse_input,
    rule_cmp,
)

from ..util import get_resource_lines

DAY = "05"

EXAMPLE_ONE = """\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
""".splitlines()


class TestPartOne:
    pass

    def test_parse_input(self):
        # want a bunch of tuples for the first part

        # then a list of list[int
        rules, updates = parse_input(EXAMPLE_ONE)

        assert rules[0] == (47, 53)
        assert rules[1] == (97, 13)
        assert rules[20] == (53, 13)

        assert updates[0] == [75, 47, 61, 53, 29]
        assert updates[5] == [97, 13, 75, 29, 47]

    def test_compare(self):
        rules, _ = parse_input(EXAMPLE_ONE)
        cmp = rule_cmp(rules)
        assert cmp(75, 47) == -1

    def test_is_ordered(self):
        rules, updates = parse_input(EXAMPLE_ONE)
        assert is_ordered(updates[0], rules)

    def test_middle_num(self):
        assert 61 == middle_num([75, 47, 61, 53, 29])

    def test_example_1(self):
        lines = EXAMPLE_ONE
        expected = 143
        actual = answer_1(lines)
        assert expected == actual

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines)
        print(f"\nAnswer 1 : {answer}\n")
        expected = 6051
        assert expected == answer


EXAMPLE_TWO = EXAMPLE_ONE


class TestPartTwo:
    pass

    def test_example_2(self):
        lines = EXAMPLE_TWO
        expected = 123
        actual = answer_2(lines)
        assert expected == actual

    def test_answer_2(self):
        lines = get_resource_lines(DAY)
        answer = answer_2(lines)
        print(f"\nAnswer 2 : {answer}\n")
        # expected =
        # assert expected == answer
