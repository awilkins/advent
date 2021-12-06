

from typing import List


def next_day(fish: List[int]) -> List[int]:

    new_fish = []
    nnf = 0
    for f in fish:
        nf = f - 1

        if nf < 0:
            nf = 6
            nnf += 1

        new_fish.append(nf)

    new_fish.extend([8] * nnf)

    return new_fish


def format_fish(fish: List[int], day: int) -> str:

    if day == 0:
        prefix = "Initial state:"
    else:
        ds = f" {day}"[-2:]
        if day > 1:
            plural = "s:"
        else:
            plural = ": "
        prefix = f"After {ds} day{plural}"

    return f"{prefix} {','.join([ str(f) for f in fish] )}"


def fish_redux(fish: List[int]) -> List[int]:
    redux = [0] * 9
    for f in fish:
        redux[f] += 1
    return redux


def next_day_redux(redux: List[int]) -> List[int]:

    next_redux = [0] * 9
    for index in range(8, -1, -1):
        next_redux[index - 1] = redux[index]

    next_redux[6] += next_redux[8]

    return next_redux


def answer_1(lines: List[str], days: int):

    fish = [int(f) for f in lines[0].split(',')]

    for day in range(days):
        fish = next_day(fish)
        # print(format_fish(fish, day + 1))

    return len(fish)


def answer_2(lines: List[str], days: int):

    fish = fish_redux([int(f) for f in lines[0].split(',')])

    for _ in range(days):
        fish = next_day_redux(fish)

    return sum(fish)
