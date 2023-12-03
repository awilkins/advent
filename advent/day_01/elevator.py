

class Elevator:

    _floor:int

    def __init__(self):
        self._floor = 0

    def execute_one(self, instruction: str):
        if instruction == "(":
            self._floor += 1

        if instruction == ")":
            self._floor -= 1

    def execute(self, instructions: str):
        for instruction in instructions:
            self.execute_one(instruction)

    def find_basement(self, instructions: str):
        for index, instruction in enumerate(instructions):
            self.execute_one(instruction)
            if self.floor() == -1:
                return index + 1

        return -1


    def floor(self) -> int:
        return self._floor


def answer_1(input: str) -> int:
    e = Elevator()
    e.execute(input)
    return e.floor()

def answer_2(input: str) -> int:
    e = Elevator()
    return e.find_basement(input)
