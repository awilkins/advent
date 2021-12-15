

from typing import List, OrderedDict, Tuple


def make_grid(lines: List[str]) -> List[List[int]]:
    return [
        [ int(c) for c in row ]
        for row in lines
    ]


def squares_in_rank(grid_size:int, rank: int) -> List[Tuple[int, int]]:
    squares_in_rank = [
        (r, rank - r) for r in range(rank + 1)
        if r < grid_size and rank - r < grid_size
    ]
    return squares_in_rank


def find_cheapest_risk(grid: List[List[int]], risk: List[List[int]], rank: int) -> List[List[int]]:

    for x, y in squares_in_rank(len(grid), rank):
        origin_risks = [
            risk[y][x] for x, y in [
                (x - 1, y),
                (x, y - 1),
            ] if x < len(grid) and y < len(grid)
                and x >=0 and y >= 0
        ] + [ 99999999999999999999999 ]

        min_risk = min(*origin_risks)
        risk[y][x] = min_risk + grid[y][x]

    return risk

def answer_1(lines: List[str]) -> int:

    grid = make_grid(lines)

    risk = [
        [0] * len(grid) for _ in range(len(grid))
    ]

    max_rank = (len(grid) - 1) * 2

    for rank in range(1, max_rank + 1):
        risk = find_cheapest_risk(grid, risk, rank)

    return risk[len(grid) - 1][len(grid) - 1]

