
from collections import deque

from typing import List, Deque





class CentralProcessingUnit:

    cycles: int
    X: int

    memory: Deque


    def __init__(self):
        self.cycles = 0
        self.X = 1
        self.memory = deque()


    def addx(self, v: int):
        self.X += v


    def noop(self):
        # empty on purpose
        pass


    def load(self, line: str):
        if line.startswith('noop'):
            self.memory.append(
                lambda self : self.noop()
            )

        if line.startswith('addx'):
            v = int(line.split(' ')[1])
            self.memory.append(
                lambda self : self.noop()
            )
            self.memory.append(
                lambda self : self.addx(v)
            )


    def load_program(self, lines: List[str]):
        for line in lines:
            self.load(line)


    def tick(self, count = 1):
        during = self.X
        signal_strength = 0
        for _ in range(count):
            during = self.X
            self.cycles += 1
            signal_strength = during * self.cycles
            instruction = self.memory.popleft()
            instruction(self)
        return during, signal_strength


def answer_1(lines: List[str]):

    cpu = CentralProcessingUnit()
    cpu.load_program(lines)

    ticks = [ 20, 40, 40, 40, 40, 40 ]

    return sum(
        s for _, s in [cpu.tick(t) for t in ticks]
    )


def answer_2(lines: List[str]):

    cpu = CentralProcessingUnit()
    cpu.load_program(lines)

    print()
    while len(cpu.memory) > 39:
        line = []
        for xx in range(40):
            aa, _ = cpu.tick()
            if aa >= xx - 1 and aa <= xx + 1:
                pix = '\u2588'
            else:
                pix = ' '
            line.append(pix)
        print("".join(line))



