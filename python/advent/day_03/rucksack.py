from collections import deque

from typing import List


def common_item(line):
    left = line[0:len(line) // 2]
    right = line[len(line) // 2 : ]

    for item in left:
        if item in right:
            return item

    return None

SCORES = ' abcdefghijklmnopqrstuvwxyz'


def score(item):

    if item in SCORES:
        return SCORES.index(item)
    else:
        return SCORES.upper().index(item) + 26



def answer_1(lines: List[str]):
    return sum(
        [score(x) for x in [
            common_item(line) for line in lines
        ]]
    )

def groups(lines):

    lines = deque(lines)
    group = []

    while lines:
        if len(group) == 3:
            yield group
            group = []
        group.append(lines.popleft())

    yield group


def group_item(group):
    one = set(group[0])
    two = set(group[1])
    three = set(group[2])

    item = one.intersection(two).intersection(three)

    assert len(item) == 1

    return item.pop()


def answer_2(lines: List[str]):
    return sum(
        [
            score(badge) for badge in [
                group_item(group) for group in groups(lines)
            ]
        ]
    )
