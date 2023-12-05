from __future__ import annotations

import json

from typing import Sequence


def search(node, double=False):

    subnodes = []

    if type(node) is dict:
        subnodes = node.values()
        if double and 'red' in node.values():
            subnodes = []

    if type(node) is list:
        subnodes = node

    for subnode in subnodes:
        subsearch = search(subnode, double)
        b = next(subsearch, None)
        while b:
            yield b
            b = next(subsearch, None)

    if type(node) is str:
        pass

    if type(node) is int:
        yield node


def answer_1(line: str):
    doc = json.loads(line)
    s = search(doc)
    return sum(s)

def answer_2(line: str):
    doc = json.loads(line)
    s = search(doc, True)
    return sum(s)
