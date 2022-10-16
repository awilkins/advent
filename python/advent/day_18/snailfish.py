
from __future__ import annotations


class Pair:

    parent: Pair | None
    left: Pair | int | None
    right: Pair | int | None


    def __init__(self, left = None, right = None, parent = None):
        self.parent = parent
        self.left = left
        self.right = right


    def replace(self, old: Pair, new: Pair | int):

        if isinstance(new, Pair):
            new.parent = self

        if self.left == old:
            self.left = new

        if self.right == old:
            self.left = new


    def __str__(self) -> str:
        return f"[{str(self.left)},{str(self.right)}]"


    def reduce(self):

        depth = 0
        current_pair = self
        while current_pair.parent:
            depth += 1
            current_pair = current_pair.parent

        if depth == 4:
            self.explode()
            return True

        if isinstance(self.left, int) and self.left >= 10:
            new_left = self.left // 2
            new_right = self.left - new_left
            self.left = Pair(new_left, new_right, self)
            return True

        if isinstance(self.right, int) and self.right >= 10:
            new_left = self.right // 2
            new_right = self.right - new_left
            self.right = Pair(new_left, new_right, self)
            return True

        return False


    @staticmethod
    def parse(line: str) -> Pair:

        current_pair: Pair | None = Pair()

        def left(p, x): p.left = x
        def right(p, x): p.right = x
        assign = left

        for c in line[1:]:

            if c == '[':
                new_pair = Pair(parent=current_pair)
                assign(current_pair, new_pair)
                assign = left
                current_pair = new_pair

            if c == ']' and current_pair.parent:
                current_pair = current_pair.parent

            if c == ',':
                assign = right

            if c.isdigit():
                assign(current_pair, int(c))

        return current_pair
