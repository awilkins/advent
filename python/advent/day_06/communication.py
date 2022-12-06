
from collections import deque

from typing import List

def detect_unique_sequence(input:str, size: int):

    index = size

    while len(set(input[index - size : index])) < size:
        index += 1

    return index

def answer_1(input: str):
    return detect_unique_sequence(input, 4)


def answer_2(input: str):
    return detect_unique_sequence(input, 14)
