from __future__ import annotations

from typing import Sequence, List, Dict

class Sue:

    name: str
    attributes: Dict[str, int]

    def __init__(self, line: str) -> None:
        parts = line.split(': ', 1)
        self.name = parts[0]

        attribute_parts = parts[1].split(', ')

        self.attributes = {}
        for att in attribute_parts:
            name, value = att.split(': ')
            value = int(value)
            self.attributes[name] = value

    def matches(self, attributes: Dict[str, int]):
        for att, value in attributes.items():
            if att in self.attributes:

                if self.attributes[att] != value:
                    return False

        return True

    def matches_v2(self, attributes: Dict[str, int]):
        for att, value in attributes.items():
            if att in self.attributes:
                if att in ['cats', 'trees']:
                    if self.attributes[att] <= value:
                        return False
                elif att in ['pomeranians', 'goldfish']:
                    if self.attributes[att] >= value:
                        return False
                elif self.attributes[att] != value:
                    return False

        return True


def answer_1(lines: Sequence[str], fingerlines: Sequence[str]):
    sues = [Sue(line) for line in lines]

    fingerprint = {
        name: int(value) for name, value in
        (line.split(': ') for line in fingerlines)
    }

    for sue in sues:
        if sue.matches(fingerprint):
            return int(sue.name.split()[1])



def answer_2(lines: Sequence[str], fingerlines: Sequence[str]):
    sues = [Sue(line) for line in lines]

    fingerprint = {
        name: int(value) for name, value in
        (line.split(': ') for line in fingerlines)
    }

    for sue in sues:
        if sue.matches_v2(fingerprint):
            return int(sue.name.split()[1])
