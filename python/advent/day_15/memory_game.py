
from itertools import repeat
from typing import Generator, List


def next_number(starting_numbers: List[int]) -> Generator[int, None, None]:
    count = 0
    number: List[int] = list(repeat(0, 30_000_000))

    last_number = 0
    for n in starting_numbers:
        count += 1
        number[n] = count
        last_number = n
        yield n

    while True:
        next_number = 0
        if number[last_number] > 0:
            next_number = count - number[last_number]
        number[last_number] = count
        count += 1
        last_number = next_number
        yield next_number


def play(number_list: str, max_count=2020):

    numbers = [int(n) for n in number_list.split(',')]

    count = 0

    for n in next_number(numbers):
        count += 1
        if count == max_count:
            return n


def main():
    print(play("2,0,1,9,5,19", 30_000_000))


if __name__ == "__main__":
    main()
