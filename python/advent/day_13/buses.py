from itertools import repeat
from functools import reduce
from math import gcd, lcm
from typing import List


def time_1(lines: List[str]):

    start = int(lines[0])
    buses = lines[1].split(',')

    time = lambda start, interval: ((start // interval) + 1) * interval
    first, bus = min([
        (time(start, int(bus)), int(bus)) for bus in buses if bus != "x"
    ])
    return (first - start) * bus

def gcd_plus_n(a, b, n):
    count = 0
    while b > n:
        a, b = b, a % b
        count += 1
    print(count)
    return a


def offset_times(start, bus_ids, multipliers):
    return [
        (bus_ids[ii] * multipliers[ii]) - ii if bus_ids[ii] > 0 else 0
        for ii in range(len(bus_ids))
    ]

def ideal_bus_value(bus_ids):
    value = 0


def bus_value(bus_ids, multipliers):
    value = 0
    start = bus_ids[0] * multipliers[0]
    for ii in range(1, bus_ids):
        value += bus_ids

def valid(start: int, times: List[int]) -> bool:
    for ii in range(len(times)):
        if times[ii] != start and times[ii] != 0:
            return False
    return True

def time_2(lines: List[str], start=0) -> int:

    bus_ids = [int(b) if b != 'x' else 0 for b in lines[1].split(',')]

    multipliers: List[int] = list(repeat(1, len(bus_ids)))
    if start == 0: start = max(bus_ids)

    o_times = offset_times(start, bus_ids, multipliers)

    while not valid(start, o_times):
        for ii in range(len(o_times)):
            t = o_times[ii]
            if t != 0 and t <= start:
                diff = start - t
                multiplier_bump = diff // bus_ids[ii]
                if diff % bus_ids[ii]:
                    multiplier_bump += 1
                multipliers[ii] = multipliers[ii] + multiplier_bump

        o_times = offset_times(start, bus_ids, multipliers)
        start = max([time for time in o_times])
        # print(o_times)

    return start

INPUT = """\
1008832
23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,449,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,13,19,x,x,x,x,x,x,x,x,x,29,x,991,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,17
"""
EXAMPLE_INPUT = """\
939
7,13,x,x,59,x,31,19
"""

if __name__ == "__main__":
    lines = INPUT.splitlines()
    print(time_2(lines, 100000000000000))



