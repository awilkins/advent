

from __future__ import annotations
from typing import TYPE_CHECKING, Dict, Iterable, List, Tuple

if TYPE_CHECKING:
    from _typeshed import SupportsNext


class Node:

    def __init__(self, data):
        self.data = data
        self.next: Node | None = None

    def __repr__(self):
        return self.data


class CompressedNode(Node):

    def __repr__(self):
        return "_"


class LinkedList:
    def __init__(self, data: SupportsNext = None):
        self.head = None
        if data is not None:
            node = Node(next(data))
            self.head = node
            datum = next(data, None)
            while datum:
                node.next = Node(datum)
                node = node.next
                datum = next(data, None)


    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return "".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


def make_chain(line: str) -> LinkedList:
    return LinkedList(iter(line))


def make_rules(lines: List[str]) -> Dict[str, str]:
    rules = {}
    for line in lines:
        seq, insert = line.split(" -> ")
        rules[seq] = insert
    return rules


def get_next_poly(poly: LinkedList, rules: Dict[str, str]) -> LinkedList:

    previous_node = Node("")
    insertions = []
    for node in poly:
        pair = str(previous_node) + str(node)
        if pair in rules:
            insertions.append(
                (previous_node, node, rules[pair])
            )
        previous_node = node

    for p, n, i in insertions:
        new_node = Node(i)
        p.next = new_node
        new_node.next = n

    return poly


def monomer_histogram(poly: Iterable[Node]) -> Dict[str, int]:
    histo = {}

    for node in poly:
        histo.setdefault(node.data, 0)
        histo[node.data] += 1

    return histo


def sorted_histo(histo: Dict[str, int]) -> List[Tuple[str, int]]:
    l = histo.items()
    l = sorted(l, key=lambda x : x[1])
    return l


def answer_1(lines: List[str], iterations=10) -> int:
    poly = make_chain(lines[0])
    rules = make_rules(lines[2:])

    for i in range(iterations):
        poly = get_next_poly(poly, rules)

    h = sorted_histo(
        monomer_histogram(poly)
    )

    return abs(h[0][1] - h[-1][1])


def answer_2(lines: List[str], iterations=10) -> int:
    pairline = lines[0]
    pairs: Dict[str, int] = {}
    prev = pairline[0]

    for c in pairline[1:]:
        pairs.setdefault(prev + c, 0)
        pairs[prev + c] += 1
        prev = c

    rules = make_rules(lines[2:])

    for _ in range(iterations):
        new_pairs = {}
        for old_pair, insert in rules.items():
            new_pairs.setdefault(old_pair[0] + insert, 0)
            new_pairs[old_pair[0] + insert] += pairs.get(old_pair, 0)
            new_pairs.setdefault(insert + old_pair[1], 0)
            new_pairs[insert + old_pair[1]] += pairs.get(old_pair, 0)

        pairs = new_pairs

    histo = {}
    for pair, count in pairs.items():
        for c in pair:
            histo.setdefault(c, 0)
            histo[c] += count

    # b/c of sliding window, everything gets counted twice except the ends
    histo[pairline[0]] += 1
    histo[pairline[-1]] += 1

    histo = { k: v // 2 for k, v in histo.items() }

    h = histo.items()
    h = sorted(h, key=lambda x : x[1])

    return abs(h[0][1] - h[-1][1])
