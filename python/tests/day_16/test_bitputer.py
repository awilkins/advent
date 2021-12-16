from unittest import TestCase

from ..util import get_resource

DAY="16"

from advent.day_16.bitputer import *

EXAMPLE_INPUT = """\
"""

class TestThing(TestCase):

    def test_example_1(self):
        expected = "110100101111111000101000"
        actual = hex_to_binary("D2FE28")
        self.assertEqual(expected, actual)

        expected = 6
        actual = answer_1(["D2FE28"])
        self.assertEqual(expected, actual)


    def test_can_cope_with_big_hex(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
        actual = hex_to_binary(lines[0])
        self.assertEqual(len(actual), len(lines[0]) * 4)


    def test_literal_packets(self):
        bits = BitStream("D2FE28")
        p = Packet.parse(bits)
        self.assertEqual(2021, p.value)


    def test_nested_packets_by_length(self):
        bits = BitStream("38006F45291200")
        p = Packet.parse(bits)
        self.assertEqual(2, len(p._subpackets))
        self.assertEqual(10, p._subpackets[0].value)
        self.assertEqual(20, p._subpackets[1].value)


    def test_nested_packets_by_count(self):
        bits = BitStream("EE00D40C823060")
        p = Packet.parse(bits)
        self.assertEqual(3, len(p._subpackets))
        self.assertEqual(1, p._subpackets[0].value)
        self.assertEqual(2, p._subpackets[1].value)
        self.assertEqual(3, p._subpackets[2].value)

    def test_version_sums(self):
        TESTS = [
            (16, "8A004A801A8002F478"),
            (12, "620080001611562C8802118E34"),
            (23, "C0015000016115A2E0802F182340"),
            (31, "A0016C880162017C3686B18A3D4780"),
        ]

        for expected, hex in TESTS:
            self.assertEqual(expected, answer_1([hex]))


    def test_packet_values(self):
        TESTS = [
            (3, "C200B40A82"),
            (54, "04005AC33890"),
            (7, "880086C3E88112"),
            (9, "CE00C43D881120"),
            (1, "D8005AC2A8F0"),
            (0, "F600BC2D8F"),
            (0, "9C005AC2F8F0"),
            (1, "9C0141080250320F1802104A08"),
        ]

        for expected, hex in TESTS:
            self.assertEqual(expected, answer_2([hex]))


    # def test_example_2(self):
    #     lines = EXAMPLE_INPUT.splitlines()
    #     expected =
    #     actual =
    #     self.assertEqual(expected, actual)

    def test_answer_1(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
        answer = answer_1(lines)
        print(f'\nAnswer 1 : {answer}\n')
        # expected =
        # self.assertEqual(expected, answer)

    def test_answer_2(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
        answer = answer_2(lines)
        print(f'\nAnswer 2 : {answer}\n')
        # expected =
        # self.assertEqual(expected, answer)

