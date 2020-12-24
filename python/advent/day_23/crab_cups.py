from __future__ import annotations

from collections import deque
from itertools import chain


from typing import Deque, Iterable, List

class Cup:

    def __init__(self, value: int, previous: Cup | None = None):
        # self.prev: Cup | None = previous
        if previous: previous.next = self
        self.next: Cup | None = None
        self.value: int = value

class Circle:

    def __init__(self, cups: Iterable[int]):

        first_cup = Cup(0)
        next_cup = first_cup
        self.length = 0
        for cupval in cups:
            next_cup = Cup(cupval, next_cup)
            self.length += 1

        # splice the circle
        real_first_cup: Cup = first_cup.next
        next_cup.next = real_first_cup

        self.current_cup = real_first_cup

        self.cups: List[Cup] = list(first_cup for _ in range(self.length + 1))
        next_cup = real_first_cup
        for _ in range(self.length + 1):
            self.cups[next_cup.value] = next_cup
            next_cup = next_cup.next

        self.one_cup = first_cup
        while self.one_cup.value != 1:
            self.one_cup = self.one_cup.next


    def __len__(self):
        return self.length

    def move(self):

        one_cup = self.current_cup.next
        two_cup = one_cup.next
        three_cup = two_cup.next

        self.current_cup.next = three_cup.next

        target = self.current_cup.value - 1
        if target < 1 : target = self.length
        while target in [cup.value for cup in [one_cup, two_cup, three_cup]]:
            target -= 1
            if target < 1 : target = self.length
        destination_cup = self.cups[target]

        three_cup.next = destination_cup.next
        destination_cup.next = one_cup

        self.current_cup = self.current_cup.next


def move(circle: Deque[int], start_index:int, move:int, high = 9) -> int:

    moved_cups = []
    start_index = start_index % len(circle)
    current_cup = circle[start_index]
    ii = (start_index + 1) % len(circle)
    for ip in range(3):
        if ii == len(circle):
            ii = 0
        cup = circle[ii]
        moved_cups.append(cup)
        circle.remove(cup)

    destination_cup = current_cup - 1
    if destination_cup == 0:
        destination_cup = high
    while destination_cup not in circle:
        destination_cup -= 1
        if destination_cup == 0:
            destination_cup = high

    destination_index = (circle.index(destination_cup) + 1)
    for cup in moved_cups[::-1]:
        circle.insert(destination_index, cup)

    next_cup_index = (circle.index(current_cup) + 1) % len(circle)
    return next_cup_index


def parse(input: str) -> Deque:
    return deque([int(c) for c in input])


def play(line: str, rounds: int= 100) -> str:

    circle = parse(line)
    high = 9

    current_cup_index = 0
    for im in range(rounds):
        current_cup_index = move(
            circle,
            current_cup_index,
            move=im + 1,
            high=high
        )

    one_index = circle.index(1)
    circle.rotate(-one_index)
    circle.popleft()
    return "".join(str(i) for i in circle)

def play2(line: str, rounds: int = 10_000_000) -> int:
    high   =  1_000_000

    cups = [int(c) for c in line]

    circle = Circle(chain(cups, range(10, high + 1)))

    count = 0
    while count < rounds:
        circle.move()
        if count % 100_000 == 0:
            print(count)
        count += 1

    return circle.one_cup.next.value * circle.one_cup.next.next.value



def main():
    circle = "389125467"
    circle = "586439172"
    print(play2(circle))


if __name__ == "__main__":
    main()







