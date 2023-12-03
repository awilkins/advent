
from typing import Sequence

class Parcel:

    l: int
    w: int
    h: int

    def __init__(self, line: str):
       self.l, self.w, self.h = [int(p) for p in line.split('x')]

    def sides(self):
        return self.l * self.w , self.w * self.h, self.h * self.l

    def perimeters(self):
        return tuple(2 * p for p in (self.l + self.w , self.w + self.h, self.h + self.l))

    def paper_area(self):
        sides = self.sides()
        area = sum(
            [side * 2 for side in sides]
        ) + min(sides)
        return area

    def volume(self):
        return self.l * self.w * self.h

    def ribbon_length(self):
        return min(self.perimeters()) + self.volume()


def answer_1(lines: Sequence[str]):
    parcels = [Parcel(line) for line in lines]
    return sum(
        [parcel.paper_area() for parcel in parcels]
    )


def answer_2(lines: Sequence[str]):
    parcels = [Parcel(line) for line in lines]
    return sum(
        [parcel.ribbon_length() for parcel in parcels]
    )

