from __future__ import annotations

from itertools import permutations

from typing import Sequence, List, NamedTuple

key_counter = 0

class Container(NamedTuple):
    size: int

def answer_1(lines: Sequence[str], target: int):
    containers = [Container(int(line)) for line in lines]

    matches = {}

    for perm in permutations(containers):
        # perm = list(perm)
        volume = 0
        for index, c in enumerate(perm):
            volume += c.size
            if volume == target:
                stack = tuple(perm[0:index + 1])
                if stack not in matches:
                    matches[stack] = stack
                break
            elif volume > target:
                break

    return matches



def answer_2(lines: Sequence[str]):
    pass
