
from itertools import chain, product

from typing import List, Set, Tuple


def make_filter(line:str) -> List[bool]:
    assert len(line) == 512
    return [
        c == '#' for c in line
    ]


Point = Tuple[int, int]


class Image:

    def __init__(self, pixels: Set[Point]) -> None:
        self.pixels = pixels

    def pixlet(self, x, y):
        return [
            [
                (x, y) in self.pixels for x in range(x - 1, x + 2)
            ] for y in range(y - 1, y + 2)
        ]


    def pixlet_window(self, x, y):
        return product(range(x - 1, x + 2), range(y - 1, y + 2))


    def boundary(self):
        min_x = min(x for x, y in self.pixels) - 3
        max_x = max(x for x, y in self.pixels) + 3
        min_y = min(y for x, y in self.pixels) - 3
        max_y = max(y for x, y in self.pixels) + 3

        return (min_x, min_y), (max_x, max_y)


    def enhanced(self, filter: List[bool]) -> 'Image':
        relevant_set: Set[Point] = set(
            chain(*[self.pixlet_window(x, y) for x, y in self.pixels])
        )

        # (min_x, min_y), (max_x, max_y) = self.boundary()

        # relevant_set: Set[Point] = set(
        #     product(range(min_x, max_x + 1), range(min_y, max_y + 1))
        # )

        new_pixels: Set[Point] = set(
            (x, y) for x, y in relevant_set if filtered_pixlet(self.pixlet(x, y), filter)
        )
        return Image(new_pixels)


    @staticmethod
    def from_data(lines: List[str]):
        pixels = set()

        for y, line in enumerate(lines):
            for x, p in enumerate(line):
                if p == '#':
                    pixels.add(
                        (x, y)
                    )

        return Image(pixels)


    def __str__(self):

        (min_x, min_y), (max_x, max_y) = self.boundary()

        return "\n".join([
            "".join([ '#' if (x, y) in self.pixels else '.' for x in range(min_x, max_x + 1)])
            for y in range(min_y, max_y + 1)
        ])


def filtered_pixlet(pixlet: List[List[bool]], filter: List[bool]) -> bool:
    binary_pixlet = "".join([
        "".join(['1' if p else '0' for p in row]) for row in pixlet
    ])
    assert len(binary_pixlet) == 9
    integer_pixlet = int(binary_pixlet, 2)
    return filter[integer_pixlet]


def answer_1(filter_data, image_data) -> int:
    f = make_filter(filter_data)
    i = Image.from_data(image_data)

    i2 = i.enhanced(f)
    i3 = i2.enhanced(f)

    print(i3)

    return len(i3.pixels)
