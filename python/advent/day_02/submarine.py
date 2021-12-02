

class Submarine:

    x: int
    depth: int
    aim: int

    def __init__(self):
        self.x = 0
        self.depth = 0
        self.aim = 0

    def execute(self, command: str):
        verb, amount = command.split(" ")
        amount = int(amount)

        if verb == "forward":
            self.x += amount

        if verb == "up":
            self.depth -= amount

        if verb == "down":
            self.depth += amount

    def execute_2(self, command: str):
        verb, amount = command.split(" ")
        amount = int(amount)

        if verb == "up":
            self.aim -= amount

        if verb == "down":
            self.aim += amount

        if verb == "forward":
            self.x += amount
            self.depth += self.aim * amount

    def product(self) -> int:
        return self.depth * self.x


def answer_1(lines) -> int:

    sub = Submarine()

    for line in lines:
        sub.execute(line)

    return sub.product()

def answer_2(lines) -> int:

    sub = Submarine()

    for line in lines:
        sub.execute_2(line)

    return sub.product()
