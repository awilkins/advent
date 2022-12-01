
from typing import List

def elf_list(lines):
    elf = []

    for line in lines:
        if len(line):
            elf.append(line)
        else:
            yield elf
            elf = []

    yield elf

def largest_calories(lines) -> int:

    elves = elf_list(lines)

    max_calories = 0
    for elf in elves:
        calories = sum(
            [int(line) for line in elf]
        )
        max_calories = max(max_calories, calories)

    return max_calories

def largest_three_calories(lines) -> List[int]:

    elves = elf_list(lines)

    elf_calories = [
        sum([int(line) for line in elf])
        for elf in elves
    ]

    elf_calories.sort(reverse=True)

    return elf_calories[0:3]


def answer_1(lines):
    return largest_calories(lines)

def answer_2(lines):
    return sum(
        largest_three_calories(lines)
    )
