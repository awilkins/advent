


from typing import List, Tuple


OPEN = "([{<"
CLOSE = ")]}>"

SCORES = {
    "": 0,
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

def validate_line(line: str) -> Tuple[bool, str]:
    """Return the first invalid char or nothing"""
    stack = []

    for c in line:
        if c in OPEN:
            stack.append(c)
        if c in CLOSE:
            check = stack.pop()
            if c != CLOSE[OPEN.index(check)]:
                return False, c

    return True, ""


def complete_line(line: str) -> str:
    stack = []

    for c in line:
        if c in OPEN:
            stack.append(c)
        if c in CLOSE:
            stack.pop()

    completion = []
    while len(stack):
        completion.append(CLOSE[OPEN.index(stack.pop())])

    return "".join(completion)


def score_completion(line: str) -> int:
    score = 0

    for c in line:
        score *= 5
        score += CLOSE.index(c) + 1

    return score


def answer_1(lines: List[str]) -> int:

    return sum([ SCORES[validate_line(line)[1]] for line in lines ])


def answer_2(lines : List[str]) -> int:

    incomplete_lines = [
        line for line in lines if validate_line(line)[0]
    ]

    scores = [
        score_completion(
            complete_line(line)
        ) for line in incomplete_lines
    ]

    scores = sorted(scores)

    middle = (len(scores) - 1) // 2
    return scores[middle]
