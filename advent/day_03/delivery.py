
from collections import deque
from itertools import repeat, chain, islice

from typing import Sequence, Deque

WEST  =  (-1,  0)
EAST  =  ( 1,  0)
NORTH =  ( 0, -1)
SOUTH =  ( 0,  1)

DIRECTIONS = {
    '<': WEST,
    '>': EAST,
    '^': NORTH,
    'v': SOUTH,
}

class World:

    def __init__(self):
        self.world: Deque[Deque[int]] = deque()
        self.world.append(deque([1]))

        self.x_offset = 0
        self.y_offset = 0
        self.x = 0
        self.y = 0

    def __str__(self):
        latlines = []
        for line in self.world:
            latlines.append("".join(str(square) for square in line))
        return "\n".join(latlines)

    def grow_east(self):
        for latitude in self.world:
            latitude.append(0)

    def grow_west(self):
        for latitude in self.world:
            latitude.appendleft(0)
        self.x_offset += 1

    def grow_south(self):
        self.world.append(
            deque(repeat(0, len(self.world[0])))
        )
    def grow_north(self):
        self.world.appendleft(
            deque(repeat(0, len(self.world[0])))
        )
        self.y_offset += 1


    def delivered_squares(self):
        return sum([1 for square in chain.from_iterable(self.world) if square])

    def deliver(self, x, y):

        ax, ay = x + self.x_offset, y + self.y_offset

        if ax >= len(self.world[0]):
            self.grow_east()

        if ax < 0:
            self.grow_west()

        if ay >= len(self.world):
            self.grow_south()

        if ay < 0:
            self.grow_north()

        ax, ay = x + self.x_offset, y + self.y_offset

        self.world[ay][ax] += 1
        self.x, self.y = x, y


class Traveller:

    x, y = 0, 0
    world: World

    def __init__(self, world):
        self.world = world

    def deliver(self, vector):
        dx, dy = vector
        x, y = self.x + dx, self.y + dy

        self.world.deliver(x, y)

        self.x, self.y = x, y

    def travel(self, line):
        for move in line:
            vector = DIRECTIONS[move]
            self.deliver(vector)


def answer_1(line: str):
    world = World()
    santa = Traveller(world)
    santa.travel(line)
    return world.delivered_squares()


def answer_2(line: str):
    santa_moves = islice(line, 0, None, 2)
    robot_moves = islice(line, 1, None, 2)

    world = World()
    santa = Traveller(world)
    robot = Traveller(world)

    santa.travel(santa_moves)
    robot.travel(robot_moves)

    return world.delivered_squares()


