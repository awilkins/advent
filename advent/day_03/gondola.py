
from typing import Sequence, List


def find_number_groups(line:str) -> List[int]:
    numbers = []
    current_number = ''
    for c in line:
        if c.isdigit():
            current_number += c
        elif current_number:
            numbers.append(int(current_number))
            current_number = ''

    if current_number:
        numbers.append(int(current_number))

    return numbers


def answer_1(lines: Sequence[str]):
    pass


def answer_2(lines: Sequence[str]):
    pass
