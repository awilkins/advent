

from typing import List, Tuple


Paper = List[Tuple[int, int]]


def create_paper(lines: List[str]) -> Tuple[Paper, List[Tuple[str, int]]]:

    paper = []
    instructions = []

    for line in lines:
        if len(line) and line[0] != 'f':
            x, y = [int(c) for c in line.split(",")]
            paper.append((x, y))
        elif len(line):
            instruction = line.split(" ")[2]
            instruction = instruction.split("=")
            instruction = (instruction[0], int(instruction[1]))
            instructions.append(instruction)

    return paper, instructions


def print_paper(paper: Paper):
    height = max([y for _, y in paper]) + 1
    width = max([x for x, _ in paper]) + 1

    p = [
        ['.'] * width for _ in range(height)
    ]

    for x, y in paper:
        p[y][x] = '\u2588'

    print()
    for line in p:
        print("".join(line))


def fold_along_y(paper: Paper, y: int) -> Paper:

    above_fold = [
        (px, py) for px, py in paper
        if py < y
    ]

    below_fold = [
        (px, y - (py - y)) for px, py in paper
        if py > y
    ]

    return above_fold + below_fold


def fold_along_x(paper: Paper, x: int) -> Paper:

    left_fold = [
        (px, py) for px, py in paper
        if px < x
    ]

    right_fold = [
        (x - (px - x), py) for px, py in paper
        if px > x
    ]

    return left_fold + right_fold


def fold(paper: Paper, instruction) -> Paper:
    axis, position = instruction
    if axis == 'x':
        return fold_along_x(paper, position)
    else:
        return fold_along_y(paper, position)


def answer_1(lines: List[str]) -> int:
    folded, instructions = create_paper(lines)
    folded = fold(folded, instructions[0])
    # print_paper(folded)
    return len(set(folded))


def answer_2(lines: List[str]):
    paper, instructions = create_paper(lines)
    for i in instructions:
        paper = fold(paper, i)

    print_paper(paper)


