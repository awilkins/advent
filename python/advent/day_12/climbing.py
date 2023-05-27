
from typing import List


def parse_chart(lines: List[str]):
    chart = []
    start = (0, 0)
    end = (0, 0)
    for iy, line in enumerate(lines):
        row = []
        chart.append(row)
        for ix, c in enumerate(line):

            if 'S' == c:
                start = (ix, iy)
                c = 'a'

            if 'E' == c:
                end = (ix, iy)
                c = 'z'

            height = ord(c)
            row.append(height)

    return chart, start, end


def is_move_ok(chart, start, move):
    x, y = start
    height = chart[y][x]
    target = (start[0] + move[0], start[1] + move[1])

    tx, ty = target

    if tx < 0 or tx >= len(chart[0]):
        return False

    if ty < 0 or ty >= len(chart):
        return False

    if (chart[ty][tx] - height) > 1:
        return False

    return True




def plot_path(chart, start, end):

    current_pos = start









def answer_1(lines: List[str]):
    pass


def answer_2(lines: List[str]):
    pass
