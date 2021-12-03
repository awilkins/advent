
from typing import List


def least_most_bits(bits_list):

    one_bit_count = [ 0 ] * len(bits_list[0])
    zero_bit_count = [ 0 ] * len(bits_list[0])

    for bits in bits_list:
        for index, bit in enumerate(bits):
            ibit = int(bit)
            one_bit_count[index] += ibit
            if ibit == 0:
                zero_bit_count[index] += 1


    low_bits = [
        "1" if zero_bit_count[index] >= one_bit_count[index] else "0"
        for index, _ in enumerate(zero_bit_count)
    ]

    high_bits = [
        "1" if one_bit_count[index] >= zero_bit_count[index] else "0"
        for index, _ in enumerate(one_bit_count)
    ]

    return low_bits, high_bits

def answer_1(lines) -> int:

    low_bits, high_bits = least_most_bits(lines)

    gamma = int("".join(high_bits), 2)
    epsilon = int("".join(low_bits), 2)

    return gamma * epsilon

LOW = 0
HIGH = 1
def keep_selection(bits_list: List[str], position: int, selection: int):

    low_bits, high_bits = least_most_bits(bits_list)

    def filter_func(x):
        if low_bits[position] == high_bits[position]:
            return int(x[position]) == selection
        else:
            if selection == LOW:
                return low_bits[position] == x[position]
            else:
                return high_bits[position] == x[position]

    return list(filter(filter_func, bits_list))


def answer_2(bits_list: List[str]) -> int:

    oxygen_bits = bits_list.copy() # MOST
    co2_bits = bits_list.copy() # LEAST

    index = 0
    while len(oxygen_bits) > 1:
        oxygen_bits = keep_selection(oxygen_bits, index, HIGH)
        index += 1

    oxy_rating = int(oxygen_bits[0], 2)

    index = 0
    while len(co2_bits) > 1:
        co2_bits = keep_selection(co2_bits, index, LOW)
        index += 1

    co2_rating = int(co2_bits[0], 2)

    return oxy_rating * co2_rating
