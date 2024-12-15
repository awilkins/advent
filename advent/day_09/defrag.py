from __future__ import annotations

from typing import Sequence, List


def generate_disk_image(disk_map: str) -> list[int]:
    files_and_space: list[int] = []
    pointer = 0
    file_id = 0
    while pointer < len(disk_map):
        size = int(disk_map[pointer])
        pointer += 1
        files_and_space.extend([file_id] * size)
        file_id += 1

        if pointer >= len(disk_map):
            break

        size = int(disk_map[pointer])
        pointer += 1
        files_and_space.extend([-1] * size)

    return files_and_space


def defrag_one_step(image: list[int]):
    img = list(image)
    rimg = reversed(img)
    for index, block in enumerate(rimg):
        if block >= 0:
            blank_index = img.index(-1)
            img[blank_index] = block
            img[len(img) - (index + 1)] = -1
            return img
    return img


def defrag(image: list[int]):
    img = list(image)
    rimg = reversed(img)
    eindex = 0
    for index, block in enumerate(rimg):
        if block >= 0:
            eindex = img.index(-1, eindex)
            bindex = len(img) - (index + 1)
            if eindex > bindex:
                break
            img[eindex] = block
            img[len(img) - (index + 1)] = -1

    return img


def checksum(image) -> int:
    return sum(a * int(b) for a, b in enumerate(image) if b >= 0)


def answer_1(line):
    image = generate_disk_image(line)
    defragged = defrag(image)
    assert len(image) == len(defragged)
    return checksum(defragged)


def answer_2(lines: Sequence[str]):
    pass
