from itertools import compress, chain

from typing import Sequence, List
def find_first_digit(line):
    for c in line:
        if c.isdigit():
            return c
    return ''

def find_last_digit(line):
    for c in line[::-1]:
        if c.isdigit():
            return c
    return ''

def find_number(line):
    return int(find_first_digit(line) + find_last_digit(line))

def answer_1(lines: Sequence[str]):
    numbers = [find_number(line) for line in lines]
    return sum(numbers)

WORDY_NUMBERS = [
    ('nineteen', 19),
    ('eighteen', 18),
    ('seventeen', 17),
    ('sixteen', 16),
    ('fifteen', 15),
    ('fourteen', 14),
    ('thirteen', 13),
    ('twelve', 12),
    ('eleven', 11),
    ('ten', 10),
    ('nine', 9),
    ('eight', 8),
    ('seven', 7),
    ('six', 6),
    ('five', 5),
    ('four', 4),
    ('three', 3),
    ('two', 2),
    ('one', 1),
]

DIGITY_NUMBERS = [(str(n), n) for n in range(9, 0, -1)]

def find_digits(line: str):
    digits: List[str|int] = [0] * len(line)


    for number, value in chain(WORDY_NUMBERS, DIGITY_NUMBERS):
        if number in line:
            first = line.index(number)
            last = line.rindex(number)

            if not digits[first]:
                digits[first] = str(value)

            if not digits[last]:
                digits[last] = str(value)

    digits = list(compress(digits, digits))
    return digits


def find_number_2(line:str):
    digits = find_digits(line)
    return int(
        str(digits[0])[0] + str(digits[-1])[-1]
    )


def answer_2(lines: Sequence[str]):
    numbers = [find_number_2(line) for line in lines]
    return sum(numbers)
