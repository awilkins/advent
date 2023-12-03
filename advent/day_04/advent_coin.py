from __future__ import annotations

from hashlib import md5

from typing import Sequence

def find_block(key: str, length=5):
    hash_output = md5(b'substandard puzzle')
    block_number = 0
    target = '0' * length
    while not hash_output.hexdigest().startswith(target):
        block_number += 1
        hash_output = md5((key + str(block_number)).encode('utf-8'))

    return block_number


def answer_1(line: str):
    return find_block(line)


def answer_2(lines: Sequence[str]):
    pass
