

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



def answer_1(lines: List[str], days: int):

    fish = [ int(f) for f in lines[0].split(',') ]

    for day in range(days):
        fish = next_day(fish)
        # print(format_fish(fish, day + 1))

    return len(fish)

