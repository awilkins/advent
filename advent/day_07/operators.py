from __future__ import annotations

from typing import Sequence, List

from itertools import product

from advent.util import get_resource_lines

Equation = tuple[int, list[int]]


def parse(lines: Sequence[str]):
    result: list[Equation] = []
    for line in lines:
        line = line.replace(":", "")
        numbers = [int(n) for n in line.split()]
        eq = (numbers[0], numbers[1:])
        result.append(eq)
    return result


def solve(equation: Equation, operators: list[str]) -> int:
    operator = iter(operators)
    stack = iter(equation[1])
    total = next(stack)
    while right := next(stack, None):
        op = next(operator)
        if op == "+":  # Add
            total += right
        if op == "*":  # Multiply
            total *= right
        if op == "|":
            total = int(str(total) + str(right))

    return total


def is_solvable(equation: Equation, operator_set="+*") -> bool:
    gap_count = len(equation[1]) - 1
    solution = equation[0]
    for operators in product(operator_set, repeat=gap_count):
        if solution == solve(equation, list(operators)):
            return True
    return False


def answer_1(lines: Sequence[str]):
    equations = parse(lines)
    return sum(eq[0] for eq in equations if is_solvable(eq))


def answer_2(lines: Sequence[str]):
    equations = parse(lines)
    return sum(eq[0] for eq in equations if is_solvable(eq, operator_set="+*|"))


if "__main__" == __name__:
    import cProfile

    lines = get_resource_lines("07")
    cProfile.run("answer = answer_2(lines)")
