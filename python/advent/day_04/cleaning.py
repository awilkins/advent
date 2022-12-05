
from typing import List

def assignment_pair(line):
    pair = line.split(',')
    left = tuple(pair[0].split('-'))
    right = tuple(pair[1].split('-'))
    return range(int(left[0]), int(left[1]) + 1), range(int(right[0]), int(right[1]) + 1)


def is_redundant(left, right):
    left = set(left)
    right = set(right)
    return left.issubset(right) or right.issubset(left)


def overlaps(left, right) -> bool:
    left = set(left)
    right = set(right)
    return len(left.intersection(right)) > 0 or len(right.intersection(left)) > 0


def answer_1(lines: List[str]):
    return sum(
        [
            is_redundant(pair[0], pair[1]) for pair in [
                assignment_pair(line) for line in lines
            ]
        ]
    )


def answer_2(lines: List[str]):
    return sum(
        [
            overlaps(pair[0], pair[1]) for pair in [
                assignment_pair(line) for line in lines
            ]
        ]
    )
