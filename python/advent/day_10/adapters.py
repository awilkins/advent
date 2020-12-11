
import itertools

from typing import AnyStr, List


def product(adapter_input: List[str]) -> int:

    adapters = list([int(x) for x in adapter_input])
    adapters.sort()

    my_adapter = adapters[-1] + 3

    adapters.append(my_adapter)

    previous_joltage = 0
    ones = 0
    threes = 0
    for a in adapters:
        joltage_delta = a - previous_joltage
        if joltage_delta == 1:
            ones += 1
        elif joltage_delta == 3:
            threes += 1
        previous_joltage = a

    return ones * threes

def choices(from_here: List[int]) -> int:
    base = from_here[0]
    ii = 1
    c = 0
    while ii < len(from_here) - 1 and from_here[ii] < base + 4:
        c += choices(from_here[ii:])
        c += 1
        ii += 1
    return c

def can_omit(adapters: List[int]) -> List[int]:
    """ Indices of adapters that can be removed """
    ii = 0
    indices = []
    while ii < len(adapters) - 2:
        ii += 1
        if adapters[ii - 1] > adapters[ii + 1] - 3:
            indices.append(ii)

    return indices


def trib(adapters: List[int]) -> int:
    x = 0
    t = 1

    for ii in range(1, len(adapters)):

        d = adapters[ii] - adapters[ii - 1]

        if d == 1:
            x += 1
        elif d == 3:
            if x == 2:
                t *= 2
            if x == 3:
                t *= 4
            if x == 4:
                t *= 7
            x = 0

    return t

def arrangements(adapter_input: List[str]) -> int:
    adapters = list([int(x) for x in adapter_input])

    adapters.append(0)
    adapters.sort()
    adapters.append(adapters[-1] + 3)

    return trib(adapters)





