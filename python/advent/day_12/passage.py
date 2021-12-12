

from typing import Dict, List, Set, Tuple
from itertools import chain


class Cave:

    _name: str
    _connections: Set[str]

    def __init__(self, name: str):
        self._name = name
        self._connections = set()


    def connect_to(self, other_cave: 'Cave'):
        self._connections.add(other_cave._name)


    def __str__(self):
        return f"{self._name} -> {self._connections}"


def build_cavemap(lines: List[str]):

    cavemap = { name: Cave(name) for name in set(chain(*[ line.split('-') for line in lines ])) }

    for connection in [line.split('-') for line in lines]:
        cavemap[connection[0]].connect_to(cavemap[connection[1]])
        cavemap[connection[1]].connect_to(cavemap[connection[0]])

    return cavemap


NULL_CAVE = Cave('NULL')

def next_paths(cavemap: Dict[str, Cave], path: List[Cave], revisit: Cave):

    for cave_name in path[-1]._connections:

        next_cave = cavemap[cave_name]
        visited = len([ cave for cave in path if cave == next_cave])
        if revisit == next_cave: visited -= 1

        if not visited > 0 or cave_name == cave_name.upper():
            yield cavemap[cave_name]


def traverse(cavemap, stack, paths, revisit = NULL_CAVE):
    np = next_paths(cavemap, stack, revisit)
    for p in np:
        stack.append(p)
        if p._name == 'end':
            paths.append(stack.copy())
            stack.pop()
            continue
        traverse(cavemap, stack, paths, revisit)
        stack.pop()


def pretty_path(path: List[Cave]) -> str:
    return ",".join([ cave._name for cave in path ])

def find_paths(cavemap: Dict[str, Cave], revisits = False):

    start = cavemap['start']

    stack = [start]
    paths = []

    traverse(cavemap, stack, paths)

    if revisits:
        small_caves = [
            cave for cave in cavemap.values()
            if
                cave._name == cave._name.lower() and
                cave._name != 'start' and
                cave._name != 'end'
        ]

        for small_cave in small_caves:
            traverse(cavemap, stack, paths, small_cave)


    spaths = [ pretty_path(path) for path in paths ]
    spaths = set(spaths)

    paths = [
        [ cavemap[cave] for cave in spath.split(',') ]
        for spath in spaths
    ]

    return paths




