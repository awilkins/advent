
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
        last_number = speak(last_number, numbers, count)

    return last_number
