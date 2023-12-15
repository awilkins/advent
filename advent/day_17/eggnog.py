from __future__ import annotations

from itertools import combinations

from typing import Sequence, List, NamedTuple

key_counter = 0

class Container(NamedTuple):
    size: int

    def __str__(self) -> str:
        return str(self.size)


def generate_container_combos(containers):
    for size in range(len(containers) + 1):
        for perm in combinations(containers, size):
            yield perm

def answer_1(lines: Sequence[str], target: int):
    containers = [Container(int(line)) for line in lines]
    combos = generate_container_combos(containers)
    return sum(1 for combo in combos if sum(c.size for c in combo) == target)


def answer_2(lines: Sequence[str], target: int):
    containers = [Container(int(line)) for line in lines]
    combos = generate_container_combos(containers)
    counts = [0] * len(containers)
    min_size = len(containers)
    for combo in combos:
        if sum(c.size for c in combo) == target:
            counts[len(combo)] += 1

    for index, count in enumerate(counts):
        if count: return count
