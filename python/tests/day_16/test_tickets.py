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

    # def test_answer_2(self):
    #     input_lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

    #     answer =
    #     print(f'\nAnswer 2 : {answer}\n')

    #     # expected =
    #     # self.assertEqual(expected, answer)

