import pytest
from unittest.mock import MagicMock

from ..util import get_resource_lines


from advent.day_17.chronospatial_computer import (
    Computer,
    answer_1,
    answer_2,
)

DAY = "17"

EXAMPLE_ONE = """\
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
""".splitlines()


class TestPartOne:
    pass

    def test_progam(self):
        c = Computer(EXAMPLE_ONE)
        assert c.program == [0, 1, 5, 4, 3, 0]

    def test_registers(self):
        c = Computer(EXAMPLE_ONE)
        assert c.register_a == 729
        assert c.register_b == 0
        assert c.register_c == 0

    def test_step(self, mocker):
        c = Computer(EXAMPLE_ONE)
        assert c.instruction_pointer == 0
        spy = mocker.spy(c, "op")
        c.step()
        spy.assert_called_once_with(0, 1)
        assert c.instruction_pointer == 2

        spy.reset_mock()
        c.step()
        assert c.instruction_pointer == 4
        spy.assert_called_once_with(5, 4)

    def test_literal_operand(self):
        c = Computer(EXAMPLE_ONE)
        assert c.literal(4) == 4

    def test_combo_operand(self):
        c = Computer(EXAMPLE_ONE)
        assert c.combo(0) == 0
        assert c.combo(1) == 1
        assert c.combo(2) == 2
        assert c.combo(3) == 3
        assert c.combo(4) == 729

        c.register_b = 420
        assert c.combo(5) == 420
        c.register_c = 71
        assert c.combo(6) == 71

    def test_adv(self, mocker):
        c = Computer()
        c.register_a = 8
        c.program = [Computer.ADV, 2]
        adv: MagicMock = mocker.spy(c, "adv")
        c.step()
        adv.assert_called_once_with(2)
        assert c.register_a == 2

    def test_bxl(self, mocker):
        c = Computer()
        c.register_b = 0b00000101
        value_to_xor = 0b00000110
        expected_xor = 0b00000011
        c.program = [Computer.BXL, value_to_xor]
        bxl: MagicMock = mocker.spy(c, "bxl")
        c.step()
        bxl.assert_called_once_with(value_to_xor)
        assert c.register_b == expected_xor

    def test_bst(self, mocker):
        c = Computer()
        c.register_b = 0b11111111
        c.program = [Computer.BST, Computer.REG_B]
        bst: MagicMock = mocker.spy(c, "bst")
        c.step()
        bst.assert_called_once_with(Computer.REG_B)
        assert c.register_b == 0b00000111

    def test_jnz(self, mocker):
        c = Computer()
        c.register_a = 0
        c.program = [Computer.JNZ, 3]
        jnz: MagicMock = mocker.spy(c, "jnz")
        c.step()
        jnz.assert_called_once_with(3)
        assert c.instruction_pointer == 2

        c.instruction_pointer = 0
        c.register_a = 1
        jnz.reset_mock()
        c.step()
        jnz.assert_called_once_with(3)
        assert c.instruction_pointer == 3

    def test_bxc(self, mocker):
        c = Computer()
        c.register_b = 0b10101011
        c.register_c = 0b01010101
        expected_xor = 0b11111110
        c.program = [Computer.BXC, 0]
        bxc = mocker.spy(c, "bxc")
        c.step()
        bxc.assert_called_once_with(0)
        assert c.register_b == expected_xor

    def test_out(self, mocker):
        c = Computer()
        c.register_c = 0b11111111
        c.program = [Computer.OUT, Computer.REG_C]
        out = mocker.spy(c, "out")
        c.step()
        out.assert_called_once_with(Computer.REG_C)
        assert c.out_buffer == [0b00000111]

    def test_bdv(self, mocker):
        c = Computer()
        c.register_a = 8
        c.program = [Computer.BDV, 2]
        bdv: MagicMock = mocker.spy(c, "bdv")
        c.step()
        bdv.assert_called_once_with(2)
        assert c.register_b == 2

    def test_cdv(self, mocker):
        c = Computer()
        c.register_a = 8
        c.program = [Computer.CDV, 2]
        cdv: MagicMock = mocker.spy(c, "cdv")
        c.step()
        cdv.assert_called_once_with(2)
        assert c.register_c == 2

    def test_example_1(self):
        lines = EXAMPLE_ONE
        expected = "4,6,3,5,6,3,5,2,1,0"
        actual = answer_1(lines)
        assert actual == expected

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines)
        print(f'\nAnswer 1 : {answer}\n')
        expected = "3,4,3,1,7,6,5,6,0"
        assert expected == answer


EXAMPLE_TWO = """\
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
""".splitlines()


class TestPartTwo:
    pass

    def test_known_example_1(self):
        c = Computer(EXAMPLE_TWO)
        c.register_a = 117440
        c.run()
        assert c.out_buffer == c.program

    def test_example_2(self):
        lines = EXAMPLE_TWO
        expected = 117440
        actual = answer_2(lines)
        assert expected == actual

    def test_answer_2(self):
        lines = get_resource_lines(DAY)
        answer = answer_2(lines)
        print(f'\nanswer 2 : {answer}\n')
        # expected =
        # assert expected == answer
