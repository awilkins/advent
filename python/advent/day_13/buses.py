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

def periodicity(start, interval, bus, column):
    new_start = 0
    new_interval = 0

    ts = start

    # First bus
    while True:
        if (ts + column) % bus == 0:
            new_start = ts
            break
        ts += interval

    # Kick it on one so the next test doesn't hit
    ts += interval

    # Next bus determines periodicity of bus alignment
    while True:
        if (ts + column) % bus == 0:
            new_interval = ts - new_start
            break
        ts += interval

    return new_start, new_interval


def time_2(lines: List[str]) -> int:

    bus_id = [int(b) if b != 'x' else 0 for b in lines[1].split(',')]

    start = 0
    interval = bus_id[0]

    for ii in range(len(bus_id)):
        bus = bus_id[ii]
        if bus != 0:
            start, interval = periodicity(start, interval, bus, ii)

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



