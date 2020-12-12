

from typing import List

#  x ---->
# y    S
# |   W+E
# v    N

VECTORS = {
    "N": (0, 1),
    "E": (1, 0),
    "W": (-1, 0),
    "S": (0, -1),
    "R": 1,
    "L": -1,
}

DIRECTIONS = {
    0: "E",
    "E": 0,
    90: "S",
    "S": "90",
    180: "W",
    "W": 180,
    270: "N",
    "N": 270,
}

class Ship:

    def __init__(self, x: int = 0, y: int = 0):

        self.x: int = x
        self.y: int = y

        self.direction: int = DIRECTIONS["E"]

        if x == 0 and y == 0:
            self.waypoint: Ship = Ship(10, 1)

    def manhattan_distance(self) -> int:

        return abs(self.x) + abs(self.y)

    def turn(self, opcode, degrees: int):
        assert(degrees % 90 == 0)
        turn_amount = degrees * VECTORS[opcode]
        self.direction = (self.direction + turn_amount) % 360

    def rotate(self, opcode, degrees):
        assert(degrees % 90 == 0)
        new_heading = (self.direction + (VECTORS[opcode] * degrees)) % 360

        while self.direction != new_heading:
            y = - self.x
            x = self.y
            self.y = y
            self.x = x
            self.turn("R", 90)

    def cardinal(self, opcode, scalar):
        dx, dy = VECTORS[opcode]
        dx *= scalar
        dy *= scalar
        self.x += dx
        self.y += dy


    def do(self, opcode, scalar):

        if opcode in [ "R", "L" ]:
            self.turn(opcode, scalar)
            return

        if opcode == "F":
            opcode = DIRECTIONS[self.direction]

        self.cardinal(opcode, scalar)


    def do_waypoint(self, opcode, scalar):

        if opcode in [ "R", "L" ]:
            self.waypoint.rotate(opcode, scalar)
            return

        if opcode != "F":
            self.waypoint.cardinal(opcode, scalar)
            return

        self.x += self.waypoint.x * scalar
        self.y += self.waypoint.y * scalar

    def navigate(self, directions: List[str]):

        for instruction in directions:
            opcode = instruction[0]
            scalar = int(instruction[1:])
            self.do(opcode, scalar)

    def navigate_by_waypoint(self, directions: List[str]):

        for instruction in directions:
            opcode = instruction[0]
            scalar = int(instruction[1:])
            self.do_waypoint(opcode, scalar)


