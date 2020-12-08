from __future__ import annotations

from typing import List


class BootComp:

    def __init__(self, program: List[str]):

        self.accumulator = 0
        self.pc = 0
        self.program = program

    def op(self) -> int:
        """ Return PC register after op """

        opcode, val = self.program[self.pc].split(" ")
        value = int(val)

        if opcode == "acc":
            self.accumulator = self.accumulator + value

        if opcode == "jmp":
            self.pc = self.pc + value
            return self.pc

        if opcode == "nop":
            pass

        self.pc = self.pc + 1
        return self.pc


    def run(self):
        trace = []

        while self.pc not in trace and self.pc != len(self.program):
            trace.append(self.pc)
            self.op()

        if self.pc in trace:
            return -1

        return 0

    def self_repair(self) -> BootComp | None:
        for i_ptr in range(len(self.program)):

            opcode, val = self.program[i_ptr].split(" ")
            new_opcode = opcode.translate(str.maketrans("nojm", "jmno"))

            new_program = self.program.copy()
            new_program[i_ptr] = " ".join([new_opcode, val])
            comp = BootComp(new_program)
            exitval = comp.run()
            if exitval == 0:
                return comp

        return None


