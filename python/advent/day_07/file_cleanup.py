
from __future__ import annotations
from typing import List, Dict, Iterator

class File():

    _name: str
    _size: int

    def __init__(self, name:str, size: int):
        self._name = name
        self._size = size

    def size(self) -> int:
        return self._size


class Directory():

    _name: str
    _parent: "Directory"
    _content: Dict[ str,  "Directory" | File ]

    def __init__(self, name:str, files):
        self._name = name
        self._content = files

    def size(self) -> int:
        return sum([ item.size() for item in self._content.values() ])


def parse(lines: List[str]):

    current_dir: Directory = Directory('/', {})
    root = current_dir

    for line in lines[2:]:

        if line.startswith('$'):
            command = line.split(' ')
            program = command[1]

            if program == 'cd':
                dirname = command[2]
                if dirname == "..":
                    current_dir = current_dir._parent
                else:
                    target = current_dir._content[dirname]
                    if isinstance(target, Directory):
                        current_dir = target
                    else:
                        raise TypeError(f"{dirname} is not a Directory")

            if program == "ls":
                current_dir._content = {}

        else:

            if line.startswith("dir"):
                dirname = line.split(" ")[1]
                new_dir = Directory(dirname, {})
                new_dir._parent = current_dir
                current_dir._content[dirname] = new_dir
            else:
                size, filename = line.split(' ')
                size = int(size)
                current_dir._content[filename] = File(filename, size)

    return root


def all_dirs(root: Directory) -> Iterator[Directory]:

    for item in root._content.values():
        if isinstance(item, Directory):
            yield item
            for subitem in all_dirs(item):
                yield subitem


def answer_1(lines: List[str]):
    root = parse(lines)

    return sum(
        [ d.size() for d in all_dirs(root) if d.size() <= 100_000 ]
    )


def answer_2(lines: List[str]):

    root = parse(lines)
    dirs = list(all_dirs(root))
    dirs = sorted(dirs, key=lambda d : d.size())

    DISK_SIZE = 70000000
    remaining_space = DISK_SIZE - root.size()
    UPDATE_SPACE = 30000000
    save_size = UPDATE_SPACE - remaining_space

    delete_me = next(d for d in dirs if d.size() >= save_size)
    return delete_me.size()
