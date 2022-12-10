from unittest import TestCase

from ..util import get_resource

DAY="10"

from advent.day_10.vcrt import *

EXAMPLE_INPUT = """\
noop
addx 3
addx -5
"""

BIG_PROGRAM = """\
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""


class TestThing(TestCase):


    def test_program_1(self):
        lines = EXAMPLE_INPUT.splitlines()
        cpu = CentralProcessingUnit()
        cpu.load_program(lines)

        assert cpu.X == 1

        cpu.tick()
        assert cpu.X == 1
        assert cpu.cycles == 1

        cpu.tick()
        assert cpu.X == 1
        assert cpu.cycles == 2

        cpu.tick()
        assert cpu.X == 4
        assert cpu.cycles == 3

        cpu.tick()
        assert cpu.X == 4
        assert cpu.cycles == 4

        cpu.tick()
        assert cpu.X == -1
        assert cpu.cycles == 5


    def test_during_1(self):
        lines = EXAMPLE_INPUT.splitlines()
        cpu = CentralProcessingUnit()
        cpu.load_program(lines)

        assert cpu.X == 1

        cpu.tick()
        assert cpu.X == 1
        assert cpu.cycles == 1

        cpu.tick()
        assert cpu.X == 1
        assert cpu.cycles == 2

        during, _ = cpu.tick()
        assert during == 1
        assert cpu.X == 4
        assert cpu.cycles == 3

        during, _ = cpu.tick()
        assert during == 4
        assert cpu.X == 4
        assert cpu.cycles == 4

        during, _ = cpu.tick()
        assert during == 4
        assert cpu.X == -1
        assert cpu.cycles == 5


    def test_signal_strength(self):
        lines = BIG_PROGRAM.splitlines()
        cpu = CentralProcessingUnit()
        cpu.load_program(lines)

        during, signal = cpu.tick(20)
        assert during == 21
        assert signal == 420


    def test_example_1(self):
        lines = BIG_PROGRAM.splitlines()
        expected = 13140
        actual = answer_1(lines)
        self.assertEqual(expected, actual)

    # def test_example_2(self):
    #     lines = EXAMPLE_INPUT.splitlines()
    #     expected =
    #     actual = answer_2(lines)
    #     self.assertEqual(expected, actual)

    def test_answer_1(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
        answer = answer_1(lines)
        print(f'\nAnswer 1 : {answer}\n')
        # expected =
        # self.assertEqual(expected, answer)

    def test_answer_2(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
        answer = answer_2(lines)
        print(f'\nAnswer 2 : {answer}\n')
        # expected =
        # self.assertEqual(expected, answer)

