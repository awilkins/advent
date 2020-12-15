
from collections import deque
from typing import Deque, Dict


def speak(number, numbers: Dict[int, Deque[int]], count) -> int:

    next_number = 0

    q = numbers.get(number, deque(maxlen=2))

    if len(q) == 2:
        next_number = q[1] - q[0]

    q = numbers.get(next_number, deque(maxlen=2))
    q.append(count)
    numbers[next_number] = q

    return next_number


def play(number_list: str, max_count=2020):

    starting_numbers = [int(n) for n in number_list.split(',')]

    numbers = {
        number: deque(maxlen=2) for number in
        starting_numbers
    }

    for ii in range(len(starting_numbers)):
        numbers[starting_numbers[ii]].append(ii + 1)

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
