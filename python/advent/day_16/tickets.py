
from itertools import chain

from typing import Dict, List, Tuple


class TicketMachine:

    def __init__(self, ruleset: List[str]):

        self.rules: Dict[str, List[List[int]]] = {}
        for rule in ruleset:
            name, rules = rule.split(': ')
            rules = rules.split(' or ')
            rules = [[int(p) for p in pair.split('-')] for pair in rules]
            self.rules[name] = rules

    def validity(self, ticket: str) -> Tuple[bool, int]:
        errors = 0
        values = [int(field) for field in ticket.split(',')]
        all_valid = True
        for value in values:
            valid = False
            for rule in self.rules.values():
                for pair in rule:
                    low, high = pair
                    if low <= value and value <= high:
                        valid = True
                        break
            if not valid:
                all_valid = False
                errors += value

        return all_valid, errors


    def scan_tickets(self, tickets: List[str]) -> int:
        """ Return error rate """
        return sum([
            self.validity(ticket)[1] for ticket in tickets
        ])


    def non_matching_fields(self, value: int) -> List[str]:
        not_matched: List[str] = []
        for name, rules in self.rules.items():
            matched = False
            for low, high in rules:
                if low <= value and value <= high:
                    matched = True

            if not matched:
                not_matched.append(name)

        return not_matched


    def field_positions(self, tickets: List[str]) -> Dict[str, int]:

        valid_tickets = [ticket for ticket in tickets if self.validity(ticket)[0]]

        parsed_tickets = [
            [int(value) for value in ticket.split(',')]
            for ticket in valid_tickets
        ]

        possible_positions: List[List[str]] = []
        for ff in range(len(parsed_tickets[0])):
            remaining_fields: List[str] = list(self.rules.keys())
            for ticket in parsed_tickets:
                not_fields = self.non_matching_fields(ticket[ff])
                assert len(not_fields) < len(self.rules)
                for field in self.non_matching_fields(ticket[ff]):
                    if field in remaining_fields:
                        remaining_fields.remove(field)
            possible_positions.append(remaining_fields)

        assert min(len(pos) for pos in possible_positions) == 1

        while max(len(pos) for pos in possible_positions) > 1:
            for ff in range(len(possible_positions)):
                fields = possible_positions[ff]
                if len(fields) == 1:
                    field = fields[0]
                    for pos in possible_positions:
                        if pos is not fields and field in pos:
                            pos.remove(field)
                            assert len(pos) > 0

        assert min(len(pos) for pos in possible_positions) == 1
        assert max(len(pos) for pos in possible_positions) == 1

        positions: Dict[str, int] = {}
        for ff in range(len(possible_positions)):
            pos = possible_positions[ff]
            positions[pos[0]] = ff

        return positions

def correct_ticket(ticket: str, positions: Dict[str, int]) -> Dict[str, int]:

    values = [int(f) for f in ticket.split(',')]

    corrected_ticket = {}
    for field, position in positions.items():
        corrected_ticket[field] = values[position]

    return corrected_ticket

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
