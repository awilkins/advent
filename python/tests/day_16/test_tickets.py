from functools import reduce
from unittest import TestCase

from ..util import get_resource

DAY="16"

from advent.day_16.tickets import *

EXAMPLE_INPUT = """\
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""

INPUT_2 = """\
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
"""

class TestThing(TestCase):

    def test_parse(self):

        rules, my_ticket, other_tickets = parse_input(EXAMPLE_INPUT.splitlines())


        expected_rules = """\
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50""".splitlines()

        expected_ticket = "7,1,14"

        expected_others = """\
7,3,47
40,4,50
55,2,20
38,6,12""".splitlines()

        self.assertEqual(expected_rules, rules)
        self.assertEqual(expected_ticket, my_ticket)
        self.assertEqual(expected_others, other_tickets)


    def test_ticket_machine_rules(self):

        rules, _, _ = parse_input(EXAMPLE_INPUT.splitlines())

        expected_rules = {
            "class": [[1,3], [5,7]],
            "row": [[6,11], [33,44]],
            "seat": [[13,40], [45,50]],
        }

        machine = TicketMachine(rules)

        self.assertEqual(expected_rules, machine.rules)

    def test_example_1(self):
        input_lines = EXAMPLE_INPUT.splitlines()

        rules, ticket, others = parse_input(input_lines)

        machine = TicketMachine(rules)
        actual = machine.scan_tickets(others)
        expected = 71

        self.assertEqual(expected, actual)

    def test_answer_1(self):
        input_lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        rules, ticket, others = parse_input(input_lines)

        machine = TicketMachine(rules)
        answer = machine.scan_tickets(others)
        print(f'\nAnswer 1 : {answer}\n')

        expected = 23044
        self.assertEqual(expected, answer)


    def test_positions(self):
        lines = INPUT_2.splitlines()

        rules, ticket, others = parse_input(lines)

        machine = TicketMachine(rules)
        actual = machine.field_positions(others)

        expected = {
            "class": 1,
            "row": 0,
            "seat": 2,
        }

        self.assertDictEqual(expected, actual)

        expected = {
            "class": 12,
            "row": 11,
            "seat": 13,
        }
        actual = correct_ticket(ticket, actual)
        self.assertDictEqual(expected, actual)


    def test_validity(self):
        input_lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
        rules, ticket, others = parse_input(input_lines)
        machine = TicketMachine(rules)

        duff_ticket = "491,927,809,195,479,538,932,554,934,911,423,716,154,814,637,97,97,0,168,397"
        valid, errors = machine.validity(duff_ticket)

        self.assertFalse(valid)


    def test_answer_2(self):
        input_lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

        rules, ticket, others = parse_input(input_lines)

        machine = TicketMachine(rules)
        field_positions = machine.field_positions(others)

        real_ticket = correct_ticket(ticket, field_positions)

        departure_fields = [
            (name, value) for name, value in real_ticket.items()
            if name[0:9] == "departure"
        ]

        assert len(departure_fields) == 6

        answer = 1
        for n, a in departure_fields:
            answer *= a

        print(f'\nAnswer 2 : {answer}\n')

        expected = 3765150732757
        self.assertEqual(expected, answer)

