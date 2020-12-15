
from itertools import repeat
from collections import deque
from typing import Deque, Dict, List, Tuple


numbers = None

def speak(number, numbers: List[int], count: int) -> int:

    next_number = 0
    index0 = number * 2
    index1 = index0 + 1

    q0 = numbers[index0] # , [0, 0])
    q1 = numbers[index1] # , [0, 0])

    if q0 and q1:
        next_number = q1 - q0

    index0 = next_number * 2
    index1 = index0 + 1
    numbers[index0] = numbers[index1]
    numbers[index1] = count

    return next_number


def play(number_list: str, max_count=2020):

    starting_numbers = [int(n) for n in number_list.split(',')]

    numbers: List[int] = list(
        repeat(0, 60000000)
    )

    for ii in range(len(starting_numbers)):
        numbers[ 2 * starting_numbers[ii]] = 0
        numbers[ 2 * starting_numbers[ii] + 1] = ii + 1

    if max_count <= len(starting_numbers): return 0
    last_number = starting_numbers[-1]
    count = len(starting_numbers)

    while count < max_count:
        count += 1
        if count % 1000000 == 0:
            print(count)
        last_number = speak(last_number, numbers, count)

    return last_number


def main():

    tests = [
        ("2,0,1,9,5,19", 1), # my puzzle input
        # ("0,3,6", 175594),
        # ("1,3,2", 2578),
        # ("2,1,3", 3544142),
        # ("1,2,3", 261214),
        # ("2,3,1", 6895259),
        # ("3,2,1", 18),
        # ("3,1,2", 362),
    ]

    for numbers, expected in tests:
        print("HOORAY")
        print(numbers, play(numbers, 30000000))


if "__main__" == __name__:
    main()
