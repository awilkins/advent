from __future__ import annotations

from typing import Sequence

def linediff(line:str):
    return len(line) - len(eval(line))


ESCAPE = str.maketrans({
    '"': '\\"',
    '\\': '\\\\'
})

def escape(line:str):
    return line.translate(ESCAPE)


def encodiff(line: str):
    return len(escape(line)) - len(line) + 2


def answer_1(lines: Sequence[str]):
    return sum(linediff(line) for line in lines)


def answer_2(lines: Sequence[str]):
    return sum(encodiff(line) for line in lines)
