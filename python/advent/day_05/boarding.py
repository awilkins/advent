
from typing import Tuple


# def old_parse_pass(boarding_pass: str) -> Tuple[int, int, int]:

#     row_low = 0
#     row_high = 127

#     column_low = 0
#     column_high = 7

#     # Front is low, Left is low
#     for binar in boarding_pass:

#         if binar == "F":
#             row_high = row_high - (((row_high - row_low) // 2) + 1)

#         if binar == "B":
#             row_low = row_low + (((row_high - row_low) // 2) + 1)

#         # print(binar, row_low, row_high)

#         if binar == "L":
#             column_high = column_high - (((column_high - column_low) // 2) + 1)

#         if binar == "R":
#             column_low = column_low + (((column_high - column_low) // 2) + 1)

#         # print(binar, column_low, column_high)

#     seat_id = row_high * 8 + column_high

#     return row_high, column_high, seat_id

def decode_int(value: str, table: str) -> int:
    """
    Kicking myself for not getting this first time around

    Just convert the pass string to binary and then to decimal
    """
    return int(value.translate(str.maketrans(table, "01")), 2)

def new_parse_pass(boarding_pass: str) -> Tuple[int, int, int]:
    row = decode_int(boarding_pass[:7], "FB")
    column = decode_int(boarding_pass[7:], "LR")
    return row, column, row * 8 + column

parse_pass = new_parse_pass

def find_spare_seat(passes):
    seat_list = list([seat_id for _, _, seat_id in passes])
    seat_list.sort()

    for index in range(len(seat_list)):
        if seat_list[index] + 1 != seat_list[index + 1]:
            return seat_list[index] + 1
