from __future__ import annotations

import re

from typing import Sequence, List

DO = ("don't()", 0, 0)
DONT = ("do()", 0, 0)
NOOP = ("noop", 0, 0)


def get_instructions(program: str, support_dodont=False) -> list[tuple[str, int, int]]:
    instructions = re.findall(r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))", program)

    for index, (instruction, _, _) in enumerate(instructions):
        if instruction == "do()":
            instructions[index] = DO if support_dodont else NOOP
        if instruction == "don't()":
            instructions[index] = DONT if support_dodont else NOOP

    return list(
        (inx, int(op1), int(op2)) for inx, op1, op2 in instructions
    )

def run_program(instructions: list[tuple[str, int, int]]):
    doing = True

    total = 0
    for instruction in instructions:
        if instruction == DONT:
            doing = False
        if instruction == DO:
            doing = True
        if doing:
            _, op1, op2 = instruction
            total += op1 * op2

    return total




def answer_1(program: str):
    muls = get_instructions(program)
    return run_program(muls)



def answer_2(program: str):
    muls = get_instructions(program, support_dodont=True)
    return run_program(muls)
