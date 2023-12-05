from __future__ import annotations

from itertools import chain
from collections import deque

from typing import Sequence

def looksay(line) -> str:

    chars = []
    pipe = deque(line)

    previous_char = pipe.popleft()
    running_total = 1
    while pipe:
        current_char = pipe.popleft()
        if current_char == previous_char:
            running_total +=1
        else:
            assert running_total < 10
            chars.append(str(running_total))
            chars.append(previous_char)
            running_total = 1
        previous_char = current_char

    assert running_total < 10
    chars.append(str(running_total))
    chars.append(previous_char)

    return "".join(chars)


def answer_1(line:str):
    for _ in range(40):
        line = looksay(line)
    return len(line)



def answer_2(line:str):
    for _ in range(50):
        line = looksay(line)
    return len(line)
