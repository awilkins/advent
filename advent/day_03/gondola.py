
from itertools import chain

from typing import Sequence, List, Iterable, Tuple


def get_all_numbers(lines: Sequence[str]) -> Iterable[Tuple[int, Tuple[int, int]]]:
    numbers: List[Tuple[int, Tuple[int, int]]] = []
    for index, line in enumerate(lines):
        for number_char in find_number_groups(line):
            numbers.append(
                ( number_char[0], (number_char[1], index) )
            )

    return numbers



def find_number_groups(line:str) -> List[Tuple[int, int]]:
    numbers = []
    current_number = ''
    current_index = -1
    for index, c in enumerate(line):
        if c.isdigit():
            if current_number == '':
                current_index = index
            current_number += c
        elif current_number:
            numbers.append(
                (int(current_number), current_index)
            )
            current_number = ''
            current_index = -1
    if current_number:
        numbers.append(
            (int(current_number), current_index)
        )
    return numbers

class Component:

    x: int
    y: int
    number: int

    def __repr__(self):
        return f"Component: {self.number} ({self.x}, {self.y})"

    _symbols: List[Tuple[str, Tuple[int, int]]] = []

    def get_adjacent_symbols(self, lines) -> List[Tuple[str, Tuple[int, int]]]:
        if not self._symbols:
            self._symbols = get_adjacent_symbols(lines, (self.number, (self.x, self.y)))
        return self._symbols

    def has_adjacent_symbol(self, lines) -> bool:
        return len(self.get_adjacent_symbols(lines)) != 0

    @property
    def linkage(self):
        if len(self._symbols):
            return self._symbols[0]
        return None

def get_all_components(lines) -> List[Component]:
    components = []

    for index, line in enumerate(lines):
        for component in find_components(line):
            component.y = index
            # HACK : initialise inner state
            component.has_adjacent_symbol(lines)
            components.append(component)


    return components

def find_components(line: str) -> Iterable[Component]:

    def create_component(number, x):
        component = Component()
        component.number = number
        component.x = x
        return component

    return [create_component(number, x) for number, x in find_number_groups(line)]


def get_adjacent_symbols(lines: Sequence[str], number_pos: Tuple[int, Tuple[int, int]]) -> List[Tuple[str, Tuple[int, int]]]:

    number, found_index, found_line = number_pos[0], number_pos[1][0], number_pos[1][1]

    s_number = str(number)

    line_min = max(0, found_line - 1)
    line_max = min(len(lines) - 1, found_line + 1)

    char_min = max(0, found_index - 1)
    char_max = min(len(lines[0]) - 1, found_index + len(s_number))

    symbols: List[Tuple[str, Tuple[int, int]]] = []

    for line_index in range(line_min, line_max + 1):
        for char_index in range(char_min, char_max + 1):
            test_char = lines[line_index][char_index]
            if test_char != '.' and not test_char.isdigit():
                symbols.append(
                    (test_char, (char_index, line_index))
                )

    return symbols

def has_adjacent_symbol(lines: Sequence[str], number_pos: Tuple[int, Tuple[int, int]]) -> bool:
    symbols = get_adjacent_symbols(lines, number_pos)
    assert len(symbols) <= 1
    return len(symbols) > 0

def answer_1(lines: Sequence[str]):
    ALL_NUMBERS = get_all_numbers(lines)
    return sum([number[0] for number in ALL_NUMBERS if has_adjacent_symbol(lines, number)])

def answer_1_c(lines: Sequence[str]):
    ALL_COMPONENTS = get_all_components(lines)
    return sum([com.number for com in ALL_COMPONENTS if com.has_adjacent_symbol(lines)])

def answer_2(lines: Sequence[str]):
    ALL_COMPONENTS = get_all_components(lines)
    geary_components = [c for c in ALL_COMPONENTS if (c.linkage and c.linkage[0] == '*')]

    def shared(that: Component, other: Component):
        if that is other:
            return False
        return that.linkage == other.linkage

    found = []
    share_pairs = []
    for that in geary_components:
        buddies = [other for other in geary_components if shared(that, other)]
        assert len(buddies) <= 1
        if len(buddies) and buddies[0] not in found:
            share_pairs.append((that, buddies[0]))
            found.append(that)
            found.append(buddies[0])

    power = sum(
        (this.number * that.number) for this, that in share_pairs
    )
    return power




