
from itertools import product
from typing import List, Tuple

def parse_trees(lines: List[str]) -> List[List[int]]:
    return [
        [ int(c) for c in line ] for line in lines
    ]


def is_visible(trees: List[List[int]], coord: Tuple[int, int]) -> bool:

    x, y = coord
    row = trees[y]
    height = row[x]

    if x == 0 or x == len(trees[0]) - 1:
        return True

    if y == 0 or y == len(trees) - 1:
        return True

    if all(row[x_east] < height for x_east in range(x + 1, len(row))):
        return True

    if all(row[x_west] < height for x_west in range(x - 1, -1, -1)):
        return True

    if all(trees[y_north][x] < height for y_north in range(y - 1, -1, -1)):
        return True

    if all(trees[y_south][x] < height for y_south in range(y + 1, len(trees))):
        return True

    return False


def answer_1(lines: List[str]):
    trees = parse_trees(lines)
    coords = product(
        range(0, len(trees[0])),
        range(0, len(trees)),
    )
    return sum(
        is_visible(trees, coord) for coord in coords
    )


def scenic_score(trees: List[List[int]], coord: Tuple[int, int]) -> int:

    x, y = coord
    height = trees[y][x]

    v_east, v_west, v_north, v_south = 0, 0, 0, 0

    look_north = y - 1
    while look_north >= 0:
        v_north += 1
        if trees[look_north][x] >= height:
            break
        look_north -= 1

    look_west = x - 1
    while look_west >= 0:
        v_west += 1
        if trees[y][look_west] >= height:
            break
        look_west -= 1

    look_east = x + 1
    while look_east < len(trees[0]):
        v_east += 1
        if trees[y][look_east] >= height:
            break
        look_east += 1

    look_south = y + 1
    while look_south < len(trees):
        v_south += 1
        if trees[look_south][x] >= height:
            break
        look_south += 1

    return v_east * v_west * v_north * v_south


def answer_2(lines: List[str]):
    trees = parse_trees(lines)
    coords = product(
        range(0, len(trees[0])),
        range(0, len(trees)),
    )
    return max(
        scenic_score(trees, coord) for coord in coords
    )
