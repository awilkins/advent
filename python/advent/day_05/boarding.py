

from typing import Tuple


def parse_pass(boarding_pass: str) -> Tuple[int, int, int]:

    row_low = 0
    row_high = 127

    column_low = 0
    column_high = 7

    # Front is low, Left is low
    for binar in boarding_pass:

        if binar == "F":
            row_high = row_high - (((row_high - row_low) // 2) + 1)

        if binar == "B":
            row_low = row_low + (((row_high - row_low) // 2) + 1)

        # print(binar, row_low, row_high)

        if binar == "L":
            column_high = column_high - (((column_high - column_low) // 2) + 1)

        if binar == "R":
            column_low = column_low + (((column_high - column_low) // 2) + 1)

        # print(binar, column_low, column_high)

    seat_id = row_high * 8 + column_high

    return row_high, column_high, seat_id

def find_spare_seat(passes):
    seat_list = list([seat_id for _, _, seat_id in passes])
    seat_list.sort()

    next_seat = seat_list.pop(0)
    last_seat = -1
    while len(seat_list):
        last_seat = next_seat
        next_seat = seat_list.pop(0)
        if next_seat - last_seat == 2:
            return last_seat + 1
