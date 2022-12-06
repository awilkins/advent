
from collections import deque

from typing import List

def detect_unique_sequence(input:str, size: int):
    buffer = deque(list(input[0:size]))

    index = size

    while len(set(buffer)) < size:
        buffer.popleft()
        buffer.append(input[index])
        index += 1

    return index

def answer_1(input: str):
    return detect_unique_sequence(input, 4)


def answer_2(input: str):
    return detect_unique_sequence(input, 14)
