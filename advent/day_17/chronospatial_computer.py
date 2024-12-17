from __future__ import annotations

from typing import Sequence, List


class Computer:
    ADV = 0
    BXL = 1
    BST = 2
    JNZ = 3
    BXC = 4
    OUT = 5
    BDV = 6
    CDV = 7

    REG_A = 4
    REG_B = 5
    REG_C = 6

    program: list[int]
    register_a: int
    register_b: int
    register_c: int

    instruction_pointer: int

    out_buffer: list[int]

    def __init__(self, lines: Sequence[str] = []) -> None:
        self.instruction_pointer = 0
        self.out_buffer = []
        for line in lines:
            if line.startswith("Program:"):
                program_s = line.split(": ")[1]
                self.program = [int(n) for n in program_s.split(",")]
            if line.startswith("Register A:"):
                self.register_a = int(line.split(": ")[1])
            if line.startswith("Register B:"):
                self.register_b = int(line.split(": ")[1])
            if line.startswith("Register C:"):
                self.register_c = int(line.split(": ")[1])

    def reset(self):
        self.out_buffer = []
        self.instruction_pointer = 0
        self.register_b = 0
        self.register_c = 0

    def run(self):
        while 0 <= self.instruction_pointer < len(self.program):
            self.step()
        return ",".join(str(n) for n in self.out_buffer)

    def step(self):
        opcode = self.program[self.instruction_pointer]
        operand = self.program[self.instruction_pointer + 1]
        rv = self.op(opcode, operand)
        if rv is None:
            self.instruction_pointer += 2
        else:
            self.instruction_pointer = rv


    def op(self, opcode, operand) -> int | None:
        match opcode:
            case Computer.ADV:
                self.adv(operand)
            case Computer.BXL:
                self.bxl(operand)
            case Computer.BST:
                self.bst(operand)
            case Computer.JNZ:
                return self.jnz(operand)
            case Computer.BXC:
                self.bxc(operand)
            case Computer.OUT:
                self.out(operand)
            case Computer.BDV:
                self.bdv(operand)
            case Computer.CDV:
                self.cdv(operand)

    def literal(self, operand: int):
        return operand

    def combo(self, operand):
        if 0 <= operand < 4:
            return operand
        if Computer.REG_A == operand:
            return self.register_a
        if Computer.REG_B == operand:
            return self.register_b
        if Computer.REG_C == operand:
            return self.register_c

        raise NotImplementedError(f"Bad operand : {operand}")

    def adv(self, operand):
        numerator = self.register_a
        denominator = 2 ** self.combo(operand)
        self.register_a = numerator // denominator

    def bxl(self, operand):
        self.register_b ^= self.literal(operand)

    def bst(self, operand):
        self.register_b = self.combo(operand) % 8

    def jnz(self, operand):
        if self.register_a != 0:
            return self.literal(operand)

    def bxc(self, _):
        self.register_b ^= self.register_c

    def out(self, operand):
        self.out_buffer.append(self.combo(operand) % 8)

    def bdv(self, operand):
        numerator = self.register_a
        denominator = 2 ** self.combo(operand)
        self.register_b = numerator // denominator

    def cdv(self, operand):
        numerator = self.register_a
        denominator = 2 ** self.combo(operand)
        self.register_c = numerator // denominator


def answer_1(lines: Sequence[str]):
    c = Computer(lines)
    return c.run()


def answer_2(lines: Sequence[str]):
    c = Computer(lines)
    a = c.register_a
    c.run()
    a = 86780000
    while c.out_buffer != c.program:
        if a % 10000 == 0:
            print(a)
        c.reset()
        a += 1
        c.register_a = a
        c.run()

    return a

