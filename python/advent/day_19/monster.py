from __future__ import annotations
from typing import Dict, Generator, List, Literal, NewType, Tuple, Union

Rule = NewType("Rule", Union[
    Literal["a"],
    Literal["b"],
    Tuple[List[int], List[int]],
    List[int],
])


BINARY = str.maketrans("ab", "01")


def convert_to_int(message: str) -> int:
    return int(message.translate(BINARY), 2)


def patch(rules):

    rules[8] = (
        [42], [42, 8]
    )

    rules[11] = (
        [42, 31], [42, 11, 31]
    )


def possible_messages(rules: Dict[int, Rule], rule: Rule, stem: str = "", stack: List[int] = []) -> Generator[str]:

    if rule == "a" or rule == "b":
        yield f'{stem}{rule}'
        return

    if isinstance(rule, List):

        next_rule = rules[rule[0]]
        for next_stem in possible_messages(rules, next_rule, stem):
            next_rules = rule[1:]
            if len(next_rules) == 0:
                yield next_stem
            else:
                yield from possible_messages(rules, next_rules, next_stem)
        return

    # Last case is the tuples
    rule0 = rule[0]
    rule1 = rule[1]

    yield from possible_messages(rules, rule0, stem)
    yield from possible_messages(rules, rule1, stem)


def parse_input(lines: List[str]) -> Tuple[Dict[Rule], List[str]]:

    ii = 0
    rules: Dict[int, str] = {}
    line = lines[ii]
    while len(line) > 0:
        index, rule = line.split(':')
        index = int(index)
        rules[index] = rule.strip()
        ii +=1
        line = lines[ii]

    new_rules: Dict[int, Rule] = {}
    for index, rule in rules.items():
        index = int(index)
        if '|' in rule:
            rule_lists: List[str] = rule.split('|')
            rule0 = list(int(r) for r in rule_lists[0].strip().split(' '))
            rule1 = list(int(r) for r in rule_lists[1].strip().split(' '))
            new_rules[index]  = (rule0, rule1)
        elif '"' in rule:
            new_rules[index] = rule.strip()[1]
        else:
            new_rules[index] = [int(r) for r in rule.split(' ')]

    ii += 1
    messages = []
    while ii < len(lines):
        line = lines[ii]
        messages.append(line)
        ii += 1

    return new_rules, messages

def convert_rule(id: int, rules: Dict[int, Rule], converted: Dict[int, str]) -> str:

    rule = rules[id]
    
    if isinstance(rule, str):
        converted[id] = rule
        return rule

    if isinstance(rule, Tuple):
        
        rule0 = []
        rules0: List[int] = rule[0]
        for r_id in rules0:
            r0 = converted.get(r_id, convert_rule(r_id, rules, converted))
            rule0.append(r0)
        
        # HACK!!!!
        r = ""
        if id in rule[1]:
            if id == 8:
                r = f"{''.join(rule0)}+"
            if id == 11:
                r = f"{rule0[0]}{rule0[1]}"
                r_repeats = []
                for ii in range(1, 7):
                    r_repeats.append(
                        f"{rule0[0] * ii}{rule0[1] * ii}"
                    )
                r = f"({'|'.join(r_repeats)})"

            converted[id] = r
            return r

        rule1 = []
        rules1: List[int] = rule[1]
        for r_id in rules1:
            r1 = converted.get(r_id, convert_rule(r_id, rules, converted))
            rule1.append(r1)
        r = f"({''.join(rule0)}|{''.join(rule1)})"
        converted[id] = r
        return r

    if isinstance(rule, List):
        rule0 = []
        for r_id in rule:
            r0 = converted.get(r_id, convert_rule(r_id, rules, converted))
            rule0.append(r0)
        r = "".join(rule0)
        converted[id] = r
        return r



def convert_rules_to_regex(rules: Dict[int, Rule]):
    converted = {}
    convert_rule(0, rules, converted)
    return f"^{converted[0]}$"