

from typing import List, Tuple


def fuel_cost(subs: List[int], target: int) -> int:
    return sum(
        [ abs(target - position) for position in subs ]
    )


def move_cost(start, end) -> int:
    distance = abs(start - end)
    return distance * (distance + 1) // 2


def real_fuel_cost(subs: List[int], target: int) -> int:
    return sum(
        [ move_cost(target, position) for position in subs ]
    )


def find_cheapest(subs: List[int], cost_func=fuel_cost) -> Tuple[int, int]:

    bottom = min(subs)
    top = max(subs)

    min_cost = 10000000000000
    min_pos = -1

    for position in range(bottom, top + 1):
        cost = cost_func(subs, position)
        if cost < min_cost:
            min_pos = position
            min_cost = cost

    return min_pos, min_cost
