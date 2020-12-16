
from itertools import chain

from typing import List, Tuple


class TicketMachine:

    def __init__(self, ruleset: List[str]):

        self.rules = {}
        for rule in ruleset:
            name, rules = rule.split(': ')
            rules = rules.split(' or ')
            rules = [[int(p) for p in pair.split('-')] for pair in rules]
            self.rules[name] = rules


    def scan_tickets(self, tickets: List[str]) -> int:
        """ Return error rate """
        errors = 0

        for ticket in tickets:
            values = [int(field) for field in ticket.split(',')]
            for value in values:
                valid = False
                for rule in self.rules.values():
                    for pair in rule:
                        low, high = pair
                        if low <= value and value <= high:
                            valid = True
                            break
                if not valid:
                    errors += value

        return errors


def parse_input(lines: List[str]) -> Tuple[ List[str], str, List[str] ]:

    rules = []

    ii = 0
    line = lines[ii]
    while len(line):
        rules.append(line)
        ii += 1
        line = lines[ii]

    ii += 2
    my_ticket = lines[ii]

    other_tickets = []
    ii += 3
    while ii < len(lines):
        line = lines[ii]
        other_tickets.append(line)
        ii += 1

    return rules, my_ticket, other_tickets
