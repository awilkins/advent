
from typing import Sequence, List

COLOUR_INDEXES = [
    'red',
    'green',
    'blue',
]



def parse_throw(throw):
    cubes = throw.split(', ')
    cube_counts = [ 0, 0, 0 ]
    for cube in cubes:
        value, colour = cube.split()
        value = int(value)
        colour_index = COLOUR_INDEXES.index(colour)
        cube_counts[colour_index] = value
    return tuple(cube_counts)

def parse_game(game):
    throws = [
        parse_throw(throw) for throw in game.split('; ')
    ]
    return throws

class Game:

    id: int
    throws: List

    def __init__(self, line):
        line_parts = line.split(': ')
        self.id = int(line_parts[0].split()[1])
        self.throws = parse_game(line_parts[1])

    def is_possible(self, red, green, blue) -> bool:
        for throw in self.throws:
            t_red, t_green, t_blue = throw
            if t_red > red or t_green > green or t_blue > blue:
                return False
        return True

    def min(self):
        red, green, blue = 0, 0, 0
        for throw in self.throws:
            t_red, t_green, t_blue = throw
            red = max(red, t_red)
            green = max(green, t_green)
            blue = max(blue, t_blue)
        return red, green, blue



def answer_1(lines: Sequence[str]):
    games = [Game(line) for line in lines]
    possible_games = [game for game in games if game.is_possible(12, 13, 14)]
    return sum(game.id for game in possible_games)

def answer_2(lines: Sequence[str]):

    def power(r, g, b):
        return r * g * b

    games = [Game(line) for line in lines]
    powers = [power(*game.min()) for game in games]
    return sum(powers)
