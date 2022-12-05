
from itertools import repeat

from typing import List, Tuple, Deque

class Command:

    count: int
    from_stack: int
    to_stack: int

    mode: str

    def __init__(self, count, from_stack, to_stack):
        self.count = count
        self.from_stack = from_stack
        self.to_stack = to_stack
        self.mode = "9000"

    def execute(self, stacks: List[List[str]]):

        if self.mode == "9000":
            for _ in range(self.count):
                stacks[self.to_stack - 1].append(
                    stacks[self.from_stack - 1].pop()
                )

        if self.mode == "9001":
            crane_stack = []
            for _ in range(self.count):
                crane_stack.append(stacks[self.from_stack -1].pop())

            for _ in range(self.count):
                stacks[self.to_stack - 1].append(crane_stack.pop())


def parse_command(line: str, mode = "9000") -> Command:
    fields = line.split(' ')
    command = Command(
        int(fields[1]),
        int(fields[3]),
        int(fields[5]),
    )
    command.mode = mode
    return command


def parse_stacks(stack_lines: List[str]) -> List[List[str]]:
    # starting with the bottom line
    line = stack_lines.pop()
    stack_count = ((len(line) - 2) // 4) + 1
    stacks: List[List[str]] = [
        list() for x in range(stack_count)
    ]

    while stack_lines:
        line = stack_lines.pop()
        for x in range(stack_count):
            crate_index = x * 4 + 1
            if line[crate_index] != ' ':
                stacks[x].append(line[crate_index])

    return stacks


def do_crane_operations(lines: List[str], mode = "9000"):

    stack_lines = []

    command_line_ix = 0

    for ix, line in enumerate(lines):

        if len(line):
            stack_lines.append(line)
        else:
            command_line_ix = ix + 1
            break

    stacks = parse_stacks(stack_lines)

    for line in lines[command_line_ix:]:
        command = parse_command(line, mode)
        command.execute(stacks)

    return "".join(
        [ stack[-1] for stack in stacks ]
    )


def answer_1(lines: List[str]):
    return do_crane_operations(lines)


def answer_2(lines: List[str]):
    return do_crane_operations(lines, "9001")
