

from typing import List


def depth_increases(input: List[str]) -> int:

    count = 0
    previous = 100000

    for line in input:
        depth = int(line)
        if depth > previous:
            count += 1

        previous = depth

    return count


def depth_windows(input: List[str]) -> int:

    depths = [ int(item) for item in input ]

    pointer = 0
    count = 0

    while pointer < len(depths) - 3:
        previous = sum(depths[ pointer : pointer + 3 ])
        pointer += 1
        current = sum(depths[ pointer : pointer + 3 ])
        if current > previous:
            count += 1

    return count
