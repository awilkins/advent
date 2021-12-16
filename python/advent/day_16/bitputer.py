

from functools import reduce
import operator

from typing import TYPE_CHECKING, List, Tuple

T_SUM = 0
T_PRODUCT = 1
T_MIN = 2
T_MAX = 3
T_LITERAL = 4
T_GT = 5
T_LT = 6
T_EQUAL = 7

LENGTH_SIZE = 0
LENGTH_PACKETS = 1

def hex_to_binary(text: str) -> str:
    return f"000000{int(text, 16):b}"[- len(text) * 4:]


class BitStream:

    pointer: int
    bits: str

    def __init__(self, hex):
        self.bits = hex_to_binary(hex)
        self.pointer = 0

    def next(self, count):
        start = self.pointer
        end = self.pointer + count
        self.pointer += count
        return self.bits[start:end]

    def next_int(self, size):
        return int(self.next(size), 2)


class Header:

    version: int
    type_id: int

    @staticmethod
    def parse(bits: BitStream) -> 'Header':
        version = bits.next_int(3)
        type_id = bits.next_int(3)

        h = Header()
        h.version = version
        h.type_id = type_id

        return h


class Packet:

    _header: Header
    _value: int
    _subpackets: List['Packet']

    @staticmethod
    def parse(bits: BitStream) -> 'Packet':
        p = Packet()
        p._header = Header.parse(bits)
        p._subpackets = []

        if p._header.type_id != T_LITERAL:
            length_type = bits.next_int(1)
            if length_type == LENGTH_SIZE:
                total_size = bits.next_int(15)
                current_pointer = bits.pointer

                while bits.pointer < current_pointer + total_size:
                    p._subpackets.append(
                        Packet.parse(bits)
                    )

            elif length_type == LENGTH_PACKETS:
                subpacket_count = bits.next_int(11)
                for _ in range(subpacket_count):
                    p._subpackets.append(
                        Packet.parse(bits)
                    )

        elif p._header.type_id == T_LITERAL:
            not_last = 1
            valbits = ""
            while not_last:
                not_last = bits.next_int(1)
                valbits += bits.next(4)
            p._value = int(valbits, 2)

        return p


    @property
    def value(self):

        t = self._header.type_id
        if t == T_LITERAL:
            return self._value

        if t == T_SUM:
            return sum([p.value for p in self._subpackets])

        if t == T_PRODUCT:
            return reduce(operator.mul, [p.value for p in self._subpackets], 1)

        if t == T_MIN:
            return min([p.value for p in self._subpackets])

        if t == T_MAX:
            return max([p.value for p in self._subpackets])

        if t == T_GT:
            assert len(self._subpackets) == 2
            return 1 if self._subpackets[0].value > self._subpackets[1].value else 0

        if t == T_LT:
            assert len(self._subpackets) == 2
            return 1 if self._subpackets[0].value < self._subpackets[1].value else 0

        if t == T_EQUAL:
            assert len(self._subpackets) == 2
            return 1 if self._subpackets[0].value == self._subpackets[1].value else 0

        raise ValueError("Not a real packet type")


def answer_1(lines: List[str]) -> int:

    bits = BitStream(lines[0])
    top_packet = Packet.parse(bits)

    def total_version(p: Packet) -> int:
        return p._header.version + sum(
            [ total_version(sub_p) for sub_p in p._subpackets ]
        )

    return total_version(top_packet)


def answer_2(lines: List[str]) -> int:
    bits = BitStream(lines[0])
    p = Packet.parse(bits)
    return p.value

