from unittest import TestCase

from ..util import get_resource

from advent.day_08.bootcomp import BootComp

EXAMPLE_1 = """\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""

class TestBootComp(TestCase):

    def test_example_program(self):
        program = EXAMPLE_1.splitlines()

        comp = BootComp(program)

        expected = 5
        exitcode = comp.run()
        actual = comp.accumulator
        self.assertEqual(exitcode, -1)
        self.assertEqual(expected, actual)


    def test_answer_1(self):
        program = get_resource('day_08/input.txt').read_text().splitlines()

        comp = BootComp(program)

        exitcode = comp.run()
        self.assertEqual(exitcode, -1)
        answer = comp.accumulator
        self.assertEqual(answer, 1749)
        print(f'\nAnswer 1 : {comp.accumulator}')

    def test_self_repair(self):
        program = EXAMPLE_1.splitlines()

        comp = BootComp(program)

        expected = 8

        exitcomp = comp.self_repair()
        actual = exitcomp.accumulator
        self.assertEqual(expected, actual)

    def test_answer_2(self):
        program = get_resource('day_08/input.txt').read_text().splitlines()

        comp = BootComp(program)

        exitcomp = comp.self_repair()
        answer = exitcomp.accumulator
        print(f'\nAnswer 2 : {answer}')

