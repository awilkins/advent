
import itertools

from typing import Iterable, List, Tuple


FLR = "."
EMP = "L"
OCC = "#"

#   x------>
#  y 0 1 2
#  |0
#  |1
#  |2
#  v

def parse_input(lines: List[str]) -> List[List[str]]:
    return list([list(line) for line in lines])

def adjacent_count(seats: List, x: int, y: int) -> int:

    low_x = x - 1
    if low_x < 0: low_x = 0

    low_y = y - 1
    if low_y < 0: low_y = 0

    high_x = x + 1
    if high_x > len(seats[0]) - 1: high_x = x

    high_y = y + 1
    if high_y > len(seats) - 1: high_y = y

    count = 0
    for ix in range(low_x, high_x + 1):
        for iy in range(low_y, high_y + 1):

            if (ix, iy) == (x, y):
                continue

            # dimensions reversed - the visual x dimension is in each line
            if seats[iy][ix] == OCC:
                count += 1

    return count

VECTORS = set(
    itertools.permutations([0, 1, 1, -1, -1], 2)
)

def visible_count(seats: List, x: int, y: int) -> int:

    high_x = len(seats[0])
    high_y = len(seats)

    count = 0
    for dx, dy in VECTORS:
        ix, iy = x, y
        ix += dx
        iy += dy
        while \
            0 <= ix and ix < high_x and \
            0 <= iy and iy < high_y:

            seat = seats[iy][ix]
            if seat in [ OCC, EMP ]:
                if seat == OCC:
                    count += 1
                break

            ix += dx
            iy += dy

    return count


class SeatGrid:

    def __init__(self, lines: List[str]):
        self.grid = parse_input(lines)
        self.visibility = adjacent_count
        self.occupancy_threshold = 4

    def _all_seats(self) -> Iterable[str]:
        return itertools.chain.from_iterable(self.grid)

    def count_occupied(self) -> int:
        return sum(
            [1 for seat in self._all_seats() if seat == OCC]
        )

    def tick(self)  -> None:
        """ copy the grid to a new grid per the rules """

        max_x = len(self.grid[0])
        max_y = len(self.grid)

        ix = 0
        iy = 0

        new_grid = []
        for iy in range(max_y):
            new_row = []
            old_row = self.grid[iy]
            for ix in range(max_x):
                count = self.visibility(self.grid, ix, iy)

                seat = old_row[ix]

                if seat == EMP and count == 0:
                    new_row.append(OCC)
                elif seat == OCC and count >= self.occupancy_threshold:
                    new_row.append(EMP)
                else:
                    new_row.append(seat)
            new_grid.append(new_row)

        self.grid = new_grid

    def settle(self, p=False):
        last_count = -1
        count = self.count_occupied()

        while count != last_count:
            last_count = count
            self.tick()
            count = self.count_occupied()
            if p:
                print("tick")
                print("0123456789")
                print(self)

    def __str__(self):
        return "\n".join(
            ["".join(row) for row in self.grid]
        )




