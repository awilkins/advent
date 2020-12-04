from typing import List, Tuple

def get_square(map_line, x):
    actual_x = x % len(map_line)
    return map_line[actual_x]

def traverse_trees(map, x_slope=3, y_slope=1) -> int:
    map_lines: List[str] = list([line.strip() for line in map])

    x = 0
    y = 0

    tree_count = 0
    while y < len(map_lines):

        if get_square(map_lines[y], x) == '#':
            tree_count += 1

        x += x_slope
        y += y_slope

    return tree_count

def multi_traverse(map_lines: List[str], slopes: List[Tuple[int, int]]) -> int:

    tree_product = 1
    for x_slope, y_slope in slopes:
        tree_product *= traverse_trees(map_lines, x_slope, y_slope)

    return tree_product
