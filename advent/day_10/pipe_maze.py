from __future__ import annotations

import sys

from itertools import repeat, chain
from collections import deque

from typing import Sequence, List, NamedTuple, Dict

class Position(NamedTuple):
    x: int
    y: int

    def __add__(self, other) -> Position:
        return Position(self[0] + other[0], self[1] + other[1])

    def __sub__(self, other) -> Vector:
        return Vector(
            self[0] - other[0], self[1] - other[1]
        )


class Vector(NamedTuple):
    x: int
    y: int

DIRECTIONS: Dict[str, Vector] = {
    "N": Vector( 0, -1),
    "S": Vector( 0, +1),
    "E": Vector(+1,  0),
    "W": Vector(-1,  0),
}

OPPOSITE: Dict[str, str] = {
    "N": "S",
    "E": "W",
    "S": "N",
    "W": "E",
}

TILE_TYPES = {
    "|": "NS",
    "-": "EW",
    "L": "NE",
    "J": "NW",
    "7": "SW",
    "F": "SE",
}

BIG_TILES = {
    ".": """\
...
...
...
""".splitlines(),
    "|": """\
.|.
.|.
.|.
""".splitlines(),
    "-": """\
...
---
...
""".splitlines(),
    "L": """\
.|.
.L-
...
""".splitlines(),
    "J": """\
.|.
-J.
...
""".splitlines(),
    "7": """\
...
-7.
.|.
""".splitlines(),
    "F": """\
...
.F-
.|.
""".splitlines(),
}

PRETTY_TILES = {
    "|": "║",
    "-": "═",
    "L": "╚",
    "J": "╝",
    "7": "╗",
    "F": "╔",
    ".": " ",
    "S": "╬"
}

class Tile:

    char: str

    def __init__(self, char: str) -> None:
        self.char = char

    def connects_at(self, direction) -> bool:
        if self.char not in TILE_TYPES:
            return False
        return direction in TILE_TYPES[self.char]

    def other_connection(self, direction):
        directions = TILE_TYPES[self.char]
        if directions[0] == direction:
            return directions[1]
        else:
            return directions[0]

    def __repr__(self):
        return PRETTY_TILES[self.char]

class Maze:

    squares: List[List[Tile]]

    def __init__(self, lines: Sequence[str]) -> None:
        self.squares = list(
            list(
                Tile(char) for char in line
            ) for line in lines
        )

    def __str__(self) -> str:
        lines = []

        def map_char(c):
            return PRETTY_TILES.get(c, c)

        for line in self.squares:
            lines.append(
                "".join(
                    map_char(c.char) for c in line
                )
            )

        return "\n".join(lines)



    def get_start(self) -> Position:

        for yy, line in enumerate(self.squares):
            for xx, tile in enumerate(line):
                if tile.char == 'S':
                    return Position(xx, yy)

        return Position(-1, -1)

    def tile(self, pos: Position):
        return self.squares[pos.y][pos.x]

    def allowed_directions(self, square: Position):
        tile = self.tile(square)
        if tile.char == 'S':
            allowed_dirs = []
            for dir in 'NSEW':
                move = DIRECTIONS[dir]
                next_tile = self.tile(square + move)
                connection_from = OPPOSITE[dir]
                if next_tile.connects_at(connection_from):
                    allowed_dirs.append(dir)

            return allowed_dirs

        else:
            return TILE_TYPES[tile.char]

    def find_loop_around_start(self) -> Position:
        start = self.get_start()
        for dir in 'NSEW':
            move = DIRECTIONS[dir]
            next_tile = self.tile(start + move)
            connection_from = OPPOSITE[dir]
            if next_tile.connects_at(connection_from):
                return start + move

        raise BrokenPipeError()

    def navigate_loop(self):
        start = self.get_start()
        next_square = self.find_loop_around_start()
        yield start

        last_dir = next(
            dir for dir, move in DIRECTIONS.items() if start + move == next_square
        )

        while next_square != start:
            yield next_square
            next_tile = self.tile(next_square)
            connected_from = OPPOSITE[last_dir]
            next_dir = next_tile.other_connection(connected_from)
            next_move = DIRECTIONS[next_dir]
            next_square = next_square + next_move
            last_dir = next_dir


DIR_CYCLE = list('NESWNESWNESW')

def rotate(dir, amount):
    new_index = DIR_CYCLE.index(dir, 4) + amount
    return DIR_CYCLE[new_index]

CORNERS = '7JFL'

class PaintBot:

    pos: Position
    dir: str
    brush: str
    fill_function: function
    maze: Maze

    def __init__(self, maze: Maze, brush: str, fill_function):
        self.fill_function = fill_function
        self.brush = brush
        self.maze = maze

    def go(self):
        loop = list(self.maze.navigate_loop())

        loop_iter = iter(loop)

        previous_square = next(loop_iter)
        while square := next(loop_iter, None):
            brush_square = square + DIRECTIONS[self.brush]
            # fix brush vector first time around
            if brush_square == previous_square:
                # S was on a corner, we want the other direction
                allowed = self.maze.allowed_directions(previous_square)
                assert len(allowed) == 2
                brush_index = allowed.index(OPPOSITE[self.brush])
                self.brush = OPPOSITE[allowed[brush_index - 1]]
                brush_square = square + DIRECTIONS[self.brush]
            if brush_square not in loop:
                self.fill_function(brush_square)

            tile = self.maze.tile(square)
            if tile.char in CORNERS:
                last_move = square - previous_square
                current_direction = next(
                    dir for dir, vector in DIRECTIONS.items() if vector == last_move
                )
                new_direction = tile.other_connection(current_direction)
                difference = DIR_CYCLE.index(new_direction,4) - DIR_CYCLE.index(current_direction, 4)
                new_brush_direction = rotate(self.brush, difference)
                self.brush = new_brush_direction
                brush_square = square + DIRECTIONS[self.brush]
                self.fill_function(brush_square)

            previous_square = square

def answer_1(lines: Sequence[str]):
    maze = Maze(lines)
    return len(list(maze.navigate_loop())) / 2


def stretch(maze: Maze) -> List[str]:
    grid = [[] for row in range(len(maze.squares) * 3)]
    for small_y_index, line in enumerate(maze.squares):
        for small_x_index, tile in enumerate(line):
            tile_char = tile.char

            if tile.char == 'S':
                allowed = "".join(maze.allowed_directions(Position(small_x_index, small_y_index)))
                tile_char = next(
                    char for char, direction
                    in TILE_TYPES.items() if direction == allowed
                )

            big_tile = BIG_TILES[tile_char]
            grid[small_y_index * 3 + 0].extend(big_tile[0])
            grid[small_y_index * 3 + 1].extend(big_tile[1])
            grid[small_y_index * 3 + 2].extend(big_tile[2])

            if tile.char == 'S':
                grid[small_y_index * 3 + 1][small_x_index * 3 + 1] = 'S'

    return list("".join(line) for line in grid)


def answer_2(lines: Sequence[str]):
    maze = Maze(lines)
    maze_size = len(maze.squares) * len(maze.squares[0])

    maze = Maze(stretch(maze))
    loop = list(maze.navigate_loop())

    painted = [
        [ 0 for _ in range(len(maze.squares[0])) ]
        for _ in range(len(maze.squares))
    ]

    def fill_2(pos: Position):
        q = deque()
        q.append(pos)

        while q:
            n = q.popleft()

            if painted[n.y][n.x]:
                continue

            painted[n.y][n.x] = 1

            allowed_directions = list('SEWN')
            if n in loop:
                allowed_directions = maze.allowed_directions(n)

            for direction in allowed_directions:
                next_square = n + DIRECTIONS[direction]
                if  0 <= next_square.x < len(painted[0]) and \
                    0 <= next_square.y < len(painted):
                    if not painted[next_square.y][next_square.x]:
                        q.append(next_square)

    fill_2(Position(0, 0))

    x_indices = range(1, len(maze.squares[0]), 3)
    y_indices = range(1, len(maze.squares), 3)

    outside = 0
    for y in y_indices:
        for x in x_indices:
            if painted[y][x]:
                outside += 1

    return maze_size - outside










