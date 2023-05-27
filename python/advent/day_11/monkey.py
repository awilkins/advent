
from typing import List, Dict, Any




class Monkey:

    number: int
    items: List[int]
    test: int
    operation: Any
    truth: int
    falsehood: int

    seen: int

    def __init__(self):
        self.seen = 0

    def see(self, item: int):
        old = item
        new = 0
        new = eval(self.operation, dict(old=old, new=new))
        return new


    def do(self, relief_factor=3):
        for item in self.items:
            item = self.see(item)
            self.seen += 1
            # relief
            item = item // relief_factor
            if item % self.test == 0:
                self.throw(self.truth, item)
            else:
                self.throw(self.falsehood, item)
        self.items = []


    def throw(self, target_number, item):
        target = monkeys[target_number]
        target.catch(item)


    def catch(self, item):
        self.items.append(item)



monkeys: Dict[int, Monkey] = {}

def parse_monkeys(lines: List[str]):

    current_monkey = Monkey()

    for line in lines:
        line = line.strip()
        if line.startswith('Monkey'):
            number = int(line.split(' ')[1].split(':')[0])
            current_monkey = Monkey()
            current_monkey.number = number
            monkeys[number] = current_monkey

        if line.startswith('Starting items:'):
            items = line.split(':')[1]
            items = [int(item) for item in items.split(',')]
            current_monkey.items = items

        if line.startswith('Operation:'):
            op = line.split(':')[1].strip()
            code = compile(op.split('=')[1].strip(), 'operation.py', 'eval')
            current_monkey.operation = code

        if line.startswith('Test:'):
            current_monkey.test = int(line.split(' ')[-1])

        if line.startswith('If true:'):
            current_monkey.truth = int(line.split(' ')[-1])

        if line.startswith('If false:'):
            current_monkey.falsehood = int(line.split(' ')[-1])

    return monkeys


def answer_1(lines: List[str]):
    global monkeys
    monkeys = {}
    parse_monkeys(lines)

    for _ in range (20):
        for monkey in [monkeys[ii] for ii in range(len(monkeys))]:
            monkey.do()

    monkey_list = list(monkeys.values())
    monkey_list.sort(key=lambda m: m.seen, reverse=True)
    return monkey_list[0].seen * monkey_list[1].seen


def answer_2(lines: List[str]):
    global monkeys
    monkeys = {}
    parse_monkeys(lines)

    for ii in range (10_000):
        for monkey in [monkeys[ii] for ii in range(len(monkeys))]:
            monkey.do(relief_factor=1)

    monkey_list = list(monkeys.values())
    monkey_list.sort(key=lambda m: m.seen, reverse=True)
    return monkey_list[0].seen * monkey_list[1].seen
