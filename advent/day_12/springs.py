from __future__ import annotations

from itertools import combinations, compress
from functools import cache
from typing import Sequence, List, Tuple

def run_lengths(springs):
    parts = springs.split('.')
    return [len(p) for p in parts if len(p)]

def is_correct(springs, counts):
    return run_lengths(springs) == counts

def pre_eliminate(springs: str, counts: List[int]):
    definitely_broke = springs.replace('?', '.')
    broken_springs = compress(
        definitely_broke.split('.'),
        definitely_broke.split('.'),
    )

def possible_arrangements_2(line: str):
    springs, counts = line.split()
    counts = [int(c) for c in counts.split(',')]

    gap_bits = gap_size(springs, counts)

    unknown_indices = [index for index, c in enumerate(springs) if c == '?']

    correct_count = 0
    for bit_positions in combinations(unknown_indices, gap_bits):
        test_string = list(springs)
        for bitp in bit_positions:
            test_string[bitp] = '.'
        test_string = "".join(test_string)
        test_string = test_string.replace('?', '#')
        if is_correct(test_string, counts):
            correct_count += 1

    return correct_count

def gap_size(springs, counts):
    potential_positions = sum(1 for c in springs if c != '.')
    definite_positions = sum(counts)
    gap_bits = potential_positions - definite_positions
    return gap_bits




def answer_1(lines: Sequence[str]):
    return sum(possible_arrangements_3(line) for line in lines)

def expanded(line:str):
    springs, counts = line.split()
    springs = "?".join([springs] * 5)
    counts = ",".join([counts] * 5)
    return " ".join([springs, counts])

def estimate(line: str):
    springs, counts = line.split()
    counts = [int(c) for c in counts.split(',')]
    return 2**gap_size(springs, counts)


@cache
def calc(springs: str, groups: tuple[int, ...]):

    if not groups:
        # Out of groups, no more matches allowed
        if '#' not in springs:
            return 1
        else:
            return 0

    if not springs:
        # Out of springs ; if we got past "out of groups", we're done
        return 0

    next_char = springs[0]
    next_group = groups[0]

    def broken():
        test_group = springs[:next_group]
        # Has to be enough space for `next_group` worth of springs
        test_group = test_group.replace('?', '#')
        if test_group != '#' * next_group:
            return 0

        if len(springs) == next_group:
            if len(groups) == 1:
                return 1 # this fits
            else:
                return 0

        if springs[next_group] in '?.':
            return calc(springs[next_group + 1:], groups[1:])

        return 0

    def working():
        # Just throw away this dot and carry on
        return calc(springs[1:], groups)

    if next_char == '#':
        output = broken()
    elif next_char == '.':
        output = working()
    elif next_char == '?':
        output = working() + broken()
    else:
        raise ValueError

    return output

def possible_arrangements_3(line:str):
    springs, counts = line.split()
    counts = tuple(int(c) for c in counts.split(','))
    return calc(springs, counts)

def estimate_2(lines):
    print("\nEstimate 1: " + str(sum(estimate(line) for line in lines)))
    print("\nEstimate 2: " + str(sum(estimate(expanded(line)) for line in lines)))

def answer_2(lines: Sequence[str]):
    return sum(
        possible_arrangements_3(expanded(line)) for line in lines
    )

################### JUNKHEAP #####################

def possible_arrangements(line:str):
    springs, counts = line.split()
    counts = [int(c) for c in counts.split(',')]

    bit_size = sum(1 for s in springs if s == '?')
    unknown_max = 2**bit_size

    format_str = '{0:0' + str(bit_size) + 'b}'
    correct_count = 0
    for ii in range(unknown_max):
        bits = iter(format_str.format(ii))
        test_springs = list(springs)
        for index, c in enumerate(test_springs):
            if c == '?':
                test_springs[index] = '#' if next(bits) == '1' else '.'
        if is_correct("".join(test_springs), counts):
            correct_count += 1

    return correct_count
