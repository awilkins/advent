
from array import array
from itertools import repeat
from typing import List


def next_number(starting_numbers: List[int], max_count: int) -> int:
    count = 0
    number = array('L', repeat(0, max_count))

    last_number = 0
    for n in starting_numbers:
        count += 1
        number[n] = count
        last_number = n
        # yield n

    while count < max_count:
        next_number = 0
        n = number[last_number]
        if n != 0:
            next_number = count - n
        number[last_number] = count
        count += 1
        last_number = next_number
        # yield next_number

    return last_number


def play(number_list: str, max_count=2020):

    numbers = [int(n) for n in number_list.split(',')]

    return next_number(numbers, max_count)


def main():
    print(play("2,0,1,9,5,19", 30_000_000))


if __name__ == "__main__":
    main()
