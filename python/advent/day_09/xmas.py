
import itertools
import collections

from typing import List


def find_xmas_flaw(xmas: List[str], preamble: int):
    q = collections.deque(maxlen=preamble)
    ixmas = [int(x) for x in xmas]

    for _ in range(preamble):
        q.append(ixmas.pop(0))

    try:
        while True:
            next_xmas = ixmas.pop(0)
            found = False
            for a, b in itertools.permutations(q, 2):
                if a + b == next_xmas:
                    found = True
            q.append(next_xmas)

            if not found:
                return next_xmas

    except IndexError:
        return -1


def find_xmas_weakness(xmas: List[str], breakval: int) -> int:
    ixmas = [int(x) for x in xmas]

    size = 1

    while True:
        size += 1
        for ix in range(len(ixmas) - size):
            break_key = ixmas[ix:ix+size]
            if(sum(break_key)) == breakval:
                return min(break_key) + max(break_key)
