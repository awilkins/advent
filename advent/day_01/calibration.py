
from itertools import compress, chain

from typing import Sequence, List

DIGIT_WORDS = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]

DIGITS = [(n, str(n)) for n in range(10)]

def digit_value(val: str) -> int:
    return DIGIT_WORDS.index(val)

def line_value(line:str, words:bool = True) -> int:
    digits: List[str] = [''] * len(line)

    token_list = DIGITS
    if words:
        token_list = chain(enumerate(DIGIT_WORDS), DIGITS)

    for value, word in token_list:

        if word in line:
            first = line.index(word)
            last = line.rindex(word)

            digits[first] = str(value)
            digits[last] = str(value)

    digits = list(compress(digits, digits))
    return int(
        digits[0][0] + digits[-1][-1]
    )


def answer_1(lines: Sequence[str]):
    values = [line_value(line, words=False) for line in lines]
    return sum(values)

def answer_2(lines: Sequence[str]):
    values = [line_value(line, words=True) for line in lines]
    return sum(values)
