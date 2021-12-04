

from typing import List, Tuple


class BingoBoard:

    won: bool

    def __init__(self, lines: List[str]):
        self._squares = [
            [ int(square) for square in row.split()]
            for row in lines if len(row) > 0
        ]
        self._marks = [ [0] * 5 for _ in range(5) ]
        self.won = False

    def locate(self, number:int) -> Tuple[bool, int, int]:
        for y, row in enumerate(self._squares):
            for x, square in enumerate(row):
                if square == number:
                    return True, x, y

        return False, -1, -1

    def unmarked_sum(self) -> int:
        ums = 0
        for y in range(5):
            for x in range(5):
                if not self._marks[y][x]:
                    ums += self._squares[y][x]

        return ums

    def mark(self, x, y) -> bool:
        """Returns true if this mark wins"""
        self._marks[y][x] = 1

        win = all(self._marks[y])
        if win:
            self.won = True
            return win

        win = all([ row[x] for row in self._marks ])
        if win: self.won = True
        return win


    def play(self, number: int) -> bool:
        """Returns True if your last play was a win"""

        found, x, y = self.locate(number)
        if not found:
            return False
        else:
            return self.mark(x, y)


def parse_boards(lines: List[str]) -> List[BingoBoard]:
    boards = []

    line_counter = 0
    while line_counter < len(lines):
        boards.append(BingoBoard(lines[line_counter:line_counter + 6]))
        line_counter += 6

    return boards

def answer_1(lines: List[str]):

    numbers = [ int(item) for item in lines[0].split(',') ]

    boards = parse_boards(lines[2:])

    for number in numbers:
        for board in boards:
            win = board.play(number)
            if win:
                score = board.unmarked_sum() * number
                return score

    return -1


def answer_2(lines: List[str]):

    numbers = [ int(item) for item in lines[0].split(',') ]

    boards = parse_boards(lines[2:])

    won = lambda board : board.won

    for number in numbers:
        for board in boards:
            if not board.won:
                win = board.play(number)
                if win and len(list(filter(won, boards))) == len(boards):
                    score = board.unmarked_sum() * number
                    return score

    return -1
