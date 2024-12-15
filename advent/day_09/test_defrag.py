import pytest

from ..util import get_resource_lines


from advent.day_09.defrag import (
    answer_1,
    answer_2,
    checksum,
    defrag,
    defrag_one_step,
    generate_disk_image,
)

DAY = "09"

EXAMPLE_ONE = "2333133121414131402"

ONE_TO_FIVE = """\
0..111....22222
02.111....2222.
022111....222..
0221112...22...
02211122..2....
022111222......
""".splitlines()


def integer_disk_image(line):
    return [int(d) if d.isdigit() else -1 for d in line]


EXAMPLE_ONE_DISK_IMG = integer_disk_image("00...111...2...333.44.5555.6666.777.888899")


class TestPartOne:
    pass

    def test_generate_disk_image(self):
        assert integer_disk_image("0..") == generate_disk_image("12")
        assert integer_disk_image("00...") == generate_disk_image("23")
        assert EXAMPLE_ONE_DISK_IMG == generate_disk_image(EXAMPLE_ONE)

    def test_defrag_one_step(self):
        disk_img: list[int] = generate_disk_image("12345")
        assert integer_disk_image(ONE_TO_FIVE[0]) == disk_img

        for index in range(1, 6):
            disk_img = defrag_one_step(disk_img)
            assert integer_disk_image(ONE_TO_FIVE[index]) == disk_img

    def test_defrag(self):
        image = generate_disk_image(EXAMPLE_ONE)
        actual = defrag(image)
        assert (
            integer_disk_image("0099811188827773336446555566..............") == actual
        )

    def test_checksum(self):
        assert 1928 == checksum(defrag(generate_disk_image(EXAMPLE_ONE)))

    def test_example_1(self):
        lines = EXAMPLE_ONE
        expected = 1928
        actual = answer_1(lines)
        assert expected == actual

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        seed = lines[0]
        assert seed[-1] == "1"
        answer = answer_1(seed)
        print(f"\nAnswer 1 : {answer}\n")
        assert answer > 89312744865
        expected = 6283170117911
        assert expected == answer


EXAMPLE_TWO = EXAMPLE_ONE


class TestPartTwo:
    pass

    # def test_example_2(self):
    #     lines = EXAMPLE_TWO
    #     expected =
    #     actual = answer_2(lines)
    #     assert expected == actual

    # def test_answer_2(self):
    #     lines = get_resource_lines(DAY)
    #     answer = answer_2(lines)
    #     print(f'\nAnswer 2 : {answer}\n')
    #     # expected =
    #     # assert expected == answer
