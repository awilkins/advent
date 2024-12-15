from __future__ import annotations

from typing import Sequence, List
import re

from math import lcm, gcd
from itertools import chain

Coord = tuple[int, int]
Vector = tuple[int, int]


class Robot:
    position: Coord
    velocity: Vector

    def __init__(self, position, velocity) -> None:
        self.position = position
        self.velocity = velocity

    def move(self):
        px, py = self.position
        vx, vy = self.velocity
        px += vx
        py += vy
        self.position = (px, py)

    def position_in_bathroom(self, size: tuple[int, int]) -> tuple[int, int]:
        return (self.position[0] % size[0], self.position[1] % size[1])


ROBOT_PATTERN = re.compile(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)")


def parse_robots(lines) -> list[Robot]:
    robots = []
    for line in lines:
        robot_match = ROBOT_PATTERN.match(line)
        assert robot_match is not None
        px, py, vx, vy = [int(n) for n in robot_match.groups()]
        robots.append(
            Robot(
                (px, py),
                (vx, vy),
            )
        )
    return robots


def is_in_quadrant(position: Coord, quad_top_left: Coord, quad_bottom_right: Coord):
    px, py = position
    tlx, tly = quad_top_left
    tbx, tby = quad_bottom_right

    return (tlx <= px < tbx) and (tly <= py < tby)


def answer_1(lines: Sequence[str], bathroom_size: tuple[int, int]):
    robots = parse_robots(lines)
    for _ in range(100):
        for robot in robots:
            robot.move()

    bsx, bsy = bathroom_size
    quadrant_size_x = bsx // 2
    quadrant_size_y = bsy // 2

    qtl = sum(
        1
        for robot in robots
        if is_in_quadrant(
            robot.position_in_bathroom(bathroom_size),
            (0, 0),
            (quadrant_size_x, quadrant_size_y),
        )
    )

    qtr = sum(
        1
        for robot in robots
        if is_in_quadrant(
            robot.position_in_bathroom(bathroom_size),
            (bsx - quadrant_size_x, 0),
            (bsx, quadrant_size_y),
        )
    )

    qbl = sum(
        1
        for robot in robots
        if is_in_quadrant(
            robot.position_in_bathroom(bathroom_size),
            (0, bsy - quadrant_size_y),
            (quadrant_size_x, bsy),
        )
    )

    qbr = sum(
        1
        for robot in robots
        if is_in_quadrant(
            robot.position_in_bathroom(bathroom_size),
            (bsx - quadrant_size_x, bsy - quadrant_size_y),
            (bsx, bsy),
        )
    )

    return qtl * qtr * qbl * qbr


def answer_2(lines: Sequence[str], bathroom_size):
    robots = parse_robots(lines)
    return gcd(
        lcm(*[robot.velocity[0] for robot in robots]),
        lcm(*[robot.velocity[1] for robot in robots]),
    )
