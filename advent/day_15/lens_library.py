from __future__ import annotations

from typing import Sequence, List, NamedTuple


class Lens(NamedTuple):
    label: str
    focal: int


class HashMap:

    boxes: list[list[Lens]]

    def __init__(self):
        self.boxes = []
        for ii in range(256):
            self.boxes.append(list())

    def __str__(self):
        lines = []
        for index, box in enumerate(self.boxes):
            if box:
                lines.append(f"Box {index}: [{'] ['.join([f'{l.label} {l.focal}' for l in box])}]")
        return "\n".join(lines)

    def step(self, line:str):
        if line[-1].isdigit():
            focal = int(line[-1])
            label = line[:-2]
            lens = Lens(label, focal)
            self.add(lens)
        else:
            label = line[:-1]
            self.remove(label)

    def remove(self, label: str):
        box = self.boxes[hash(label)]
        for index, value in enumerate(box):
            if value.label == label:
                del box[index]
                return

    def add(self, lens: Lens):
        box = self.boxes[hash(lens.label)]
        for index, value in enumerate(box):
            if value.label == lens.label:
                box[index] = lens
                return
        box.append(lens)

    def focal_power(self):

        def lens_power(lens: Lens, box_index: int, slot_index: int):
            return (1 + box_index) * (slot_index + 1) * lens.focal

        total_power = 0
        for box_index, box in enumerate(self.boxes):
            for slot_index, slot in enumerate(box):
                total_power += lens_power(slot, box_index, slot_index)

        return total_power


def hash(line: str) -> int:
    current = 0
    for c in line:
        code = ord(c)
        current += code
        current *= 17
        current %= 256
    return current


def answer_1(lines: Sequence[str]):
    return sum(hash(step) for step in lines[0].split(","))


def answer_2(lines: Sequence[str]):
    hashmap = HashMap()
    for step in lines[0].split(','):
        hashmap.step(step)

    return hashmap.focal_power()

