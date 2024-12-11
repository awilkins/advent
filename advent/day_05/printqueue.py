from __future__ import annotations

from typing import Sequence
from functools import cmp_to_key


def generate_rules(line_iter):
    line = next(line_iter)
    while len(line) > 0:
        a, b = line.split("|")
        yield (int(a), int(b))
        line = next(line_iter)


def rule_cmp(rules):
    def cmp(a, b):
        rule_iter = filter(lambda r: a in r and b in r, rules)
        rule = next(rule_iter)
        if rule == (a, b):
            return -1
        else:
            return 1

    return cmp


def sorted_row(row, rules):
    cmp = rule_cmp(rules)
    return sorted(row, key=cmp_to_key(cmp))


def is_ordered(row, rules):
    sr = sorted_row(row, rules)
    return row == sr


def generate_updates(line_iter):
    try:
        while line := next(line_iter):
            yield list(int(n) for n in line.split(","))
    except StopIteration:
        return


def parse_input(lines: Sequence[str]):
    line_iter = iter(lines)
    rules = list(generate_rules(line_iter))
    updates = list(generate_updates(line_iter))

    return rules, updates


def middle_num(row):
    return row[(len(row) // 2)]


def answer_1(lines: Sequence[str]):
    rules, updates = parse_input(lines)

    return sum(middle_num(row) for row in updates if is_ordered(row, rules))


def answer_2(lines: Sequence[str]):
    rules, updates = parse_input(lines)
    bad_rows = [row for row in updates if not is_ordered(row, rules)]
    sorted_rows = [sorted_row(row, rules) for row in bad_rows]
    return sum(middle_num(row) for row in sorted_rows)
