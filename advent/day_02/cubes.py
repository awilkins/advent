
from typing import Sequence, List

THROW_INDEX = {
    'red': 0,
    'green': 1,
    'blue': 2,
}

class Game:

    id: int
    throws: List[List[int]]

    def __init__(self, line: str):
        self.id = int(line.split(':')[0].split(' ')[1])
        throws = line.split(':')[1].strip().split(';')
        self.throws = []
        for throw in throws:
            throw_counts: List[int] = [ 0, 0, 0 ]
            for group in throw.split(','):
                count, colour = group.strip().split(' ')
                count = int(count)
                index = THROW_INDEX[colour]
                throw_counts[index] = count
            self.throws.append(throw_counts)

    def is_possible(self, red: int, green: int, blue: int):
        for throw in self.throws:
            t_red, t_green, t_blue = throw
            if t_red > red or t_green > green or t_blue > blue:
                return False
        return True

    def min_cubes(self):
        red, green, blue = 0, 0, 0
        for throw in self.throws:
            t_red, t_green, t_blue = throw
            red = max(red, t_red)
            green = max(green, t_green)
            blue = max(blue, t_blue)
        return red, green, blue


def answer_1(lines: Sequence[str]):
    games = [Game(line) for line in lines]
    possible = [game for game in games if game.is_possible(12, 13, 14)]
    return sum(game.id for game in possible)

def answer_2(lines: Sequence[str]):

    def power(r, g, b):
        return r * g * b

    games = [Game(line) for line in lines]
    powers = [power(*game.min_cubes()) for game in games]
    return sum(powers)


