
from typing import List

SEG_COUNTS = [
    6,  # 0
    2,  # 1 *
    5,  # 2
    5,  # 3
    4,  # 4 *
    5,  # 5
    6,  # 6
    3,  # 7 *
    7,  # 8 *
    6,  # 9
]

A, B, C, D, E, F, G = [0, 1, 2, 3, 4, 5, 6]

UNIQUE = [1, 4, 7, 8]
UNIQUE_COUNTS = [SEG_COUNTS[u] for u in UNIQUE]


def complement(segments):
    all_segments = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    return list(filter(lambda x: x not in segments, all_segments))


def deduce_signal_map(digits: List[str]) -> List[str]:

    def digits_of_len(length: int):
        return filter(lambda d: len(d) == length, digits)

    signals = [""] * 10
    segment_map = [""] * 10

    for digit, count in zip(UNIQUE, UNIQUE_COUNTS):
        signals[digit] = next(digits_of_len(count))

    EG = complement(set(signals[4] + signals[7]))

    NINE = next(
        filter(
            lambda d: complement(d)[0] in EG,
            digits_of_len(SEG_COUNTS[9]),
        )
    )

    signals[9] = NINE

    segment_map[E] = complement(NINE)[0]

    TWO = next(
        filter(
            lambda d: segment_map[E] in d,
            digits_of_len(SEG_COUNTS[2])
        )
    )

    signals[2] = TWO
    segment_map[B] = complement(set(signals[2] + signals[7]))[0]

    FIVE = next(
        filter(
            lambda d: segment_map[B] in d,
            digits_of_len(SEG_COUNTS[5]),
        )
    )

    signals[5] = FIVE
    segment_map[C] = set(NINE).difference(set(FIVE)).pop()

    SIX = next(
        filter(
            lambda d: segment_map[C] not in d,
            digits_of_len(SEG_COUNTS[6]),
        )
    )
    signals[6] = SIX

    ZERO = set(digits_of_len(SEG_COUNTS[0])).difference(
        [signals[6], signals[9]]).pop()
    signals[0] = ZERO

    THREE = next(
        filter(
            lambda d: d not in [signal for signal in signals if len(signal)],
            digits,
        )
    )
    signals[3] = THREE

    return [''.join(sorted(s)) for s in signals]


def get_value(line: str) -> int:

    digits, number = line.split("|")
    signal_map = deduce_signal_map(digits.split())

    numbers = []
    number_list = [''.join(sorted(n)) for n in number.split()]
    for digit in number_list:
        numbers.append(signal_map.index(digit))

    value = int(''.join([str(n) for n in numbers]))
    return value


def unique_count(line: str) -> int:

    output_parts = line.split("|")[1].strip().split()
    return sum([1 for o in output_parts if len(o) in UNIQUE_COUNTS])


def count_unique(lines: List[str]):
    return sum([unique_count(line) for line in lines])
