from unittest import TestCase

from ..util import get_resource

DAY="12"

from advent.day_12.passage import *

EXAMPLE_INPUT = """\
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""

EXAMPLE_2 = """\
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
"""

EXAMPLE_3 = """\
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
"""


class TestThing(TestCase):

    def test_example_1(self):
        lines = EXAMPLE_INPUT.splitlines()
        cavemap = build_cavemap(lines)
        expected = 10
        paths = find_paths(cavemap)
        print("\n".join([ f"{pretty_path(p)}" for p in paths]))
        actual = len(paths)
        self.assertEqual(expected, actual)

    def test_example_2(self):
        lines = EXAMPLE_2.splitlines()
        cavemap = build_cavemap(lines)
        expected = 19
        paths = find_paths(cavemap)
        print("\n".join([ f"{pretty_path(p)}" for p in paths]))
        actual = len(paths)
        self.assertEqual(expected, actual)

    def test_example_3(self):
        lines = EXAMPLE_3.splitlines()
        cavemap = build_cavemap(lines)
        expected = 226
        paths = find_paths(cavemap)
        print("\n".join([ f"{pretty_path(p)}" for p in paths]))
        actual = len(paths)
        self.assertEqual(expected, actual)

    def test_answer_1(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
        cavemap = build_cavemap(lines)
        answer = len(find_paths(cavemap))
        print(f'\nAnswer 1 : {answer}\n')

        # expected =
        # self.assertEqual(expected, answer)

    # def test_answer_2(self):
    #     lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

    #     answer =
    #     print(f'\nAnswer 2 : {answer}\n')

    #     # expected =
    #     # self.assertEqual(expected, answer)

