
from itertools import chain

from typing import Sequence, List, Iterable, Tuple


def get_all_numbers(lines: Sequence[str]) -> Iterable[Tuple[int, Tuple[int, int]]]:
    numbers: List[Tuple[int, Tuple[int, int]]] = []
    for index, line in enumerate(lines):
        for number_char in find_number_groups(line):
            numbers.append(
                ( number_char[0], (number_char[1], index) )
            )

    return numbers

def find_number_groups(line:str) -> List[Tuple[int, int]]:
    numbers = []
    current_number = ''
    current_index = -1
    for index, c in enumerate(line):
        if c.isdigit():
            if current_number == '':
                current_index = index
            current_number += c
        elif current_number:
            numbers.append(
                (int(current_number), current_index)
            )
            current_number = ''
            current_index = -1
    if current_number:
        numbers.append(
            (int(current_number), current_index)
        )
    return numbers

def has_adjacent_symbol(lines: Sequence[str], number_pos: Tuple[int, Tuple[int, int]]) -> bool:

    number, found_index, found_line = number_pos[0], number_pos[1][0], number_pos[1][1]

    s_number = str(number)

    line_min = max(0, found_line - 1)
    line_max = min(len(lines) - 1, found_line + 1)

    char_min = max(0, found_index - 1)
    char_max = min(len(lines[0]) - 1, found_index + len(s_number))

    for line_index in range(line_min, line_max + 1):
        for char_index in range(char_min, char_max + 1):
            test_char = lines[line_index][char_index]
            if test_char != '.' and not test_char.isdigit():
                return True

    return False


def answer_1(lines: Sequence[str]):
    ALL_NUMBERS = get_all_numbers(lines)
    return sum([number[0] for number in ALL_NUMBERS if has_adjacent_symbol(lines, number)])

def answer_2(lines: Sequence[str]):
    pass
