from unittest import TestCase

from ..util import get_resource

from advent.day_05.boarding import find_spare_seat, parse_pass

EXAMPLES = [
    # PASS, ROW, COL, SEAT_ID
    [ "FBFBBFFRLR", 44, 5, 357 ],
    [ "BFFFBBFRRR", 70, 7, 567 ],
    [ "FFFBBBFRRR", 14, 7, 119 ],
    [ "BBFFBBFRLL", 102, 4, 820 ],
]

PASS_DATA = get_resource('day_05/input.txt').read_text().splitlines()

class TestBoarding(TestCase):

    def test_examples(self):
        for boarding_pass, row, column, seat_id in EXAMPLES:
            expected_row, expected_column, expected_seat_id = parse_pass(boarding_pass)
            self.assertEqual(row, expected_row)
            self.assertEqual(column, expected_column)
            self.assertEqual(seat_id, expected_seat_id)

    def test_answer_1(self):
        passes = [parse_pass(datum) for datum in PASS_DATA]

        high_id = max(
            [seat_id for _, _, seat_id in passes]
        )

        print(f"\nAnswer 01: {high_id}")

    def test_answer_2(self):
        passes = [parse_pass(datum) for datum in PASS_DATA]

        print(f"\nAnswer 02: {find_spare_seat(passes)}")
