from __future__ import annotations

from functools import reduce

from ..util import get_resource_lines

from typing import Sequence

DAY="06"

def race_distance(race_time, push_time):
    return (race_time - push_time) * push_time

def race_winners(time, distance):
    winners = 0

    min_speed = distance // time

    for speed in range(min_speed, time):
        # if race_distance(time, speed) > distance:
        if (time - speed) * speed > distance:
            winners += 1

    return winners


def answer_1(lines: Sequence[str]):
    times = [int(time) for time in lines[0].split()[1:]]
    distances = [int(time) for time in lines[1].split()[1:]]

    winning_ways = [
        race_winners(time, distance) for time, distance in zip(times, distances)
    ]

    return reduce(lambda x, y: x * y, winning_ways)


def answer_2(lines: Sequence[str]):
    time = int("".join(lines[0].split()[1:]))
    distance = int("".join(lines[1].split()[1:]))

    winning_ways = race_winners(time, distance)
    return winning_ways


if __name__ == "__main__":
    lines = get_resource_lines(DAY)
    answer = answer_2(lines)
    print(f'\nAnswer 2 : {answer}\n')
