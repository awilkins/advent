from unittest import TestCase

from ..util import get_resource

DAY="07"

from advent.day_07.file_cleanup import *

EXAMPLE_INPUT = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

class TestThing(TestCase):

    def test_root_size(self):
        lines = EXAMPLE_INPUT.splitlines()
        expected = 48381165
        actual = parse(lines).size()
        self.assertEqual(expected, actual)

    def test_example_1(self):
        lines = EXAMPLE_INPUT.splitlines()
        expected = 95437
        actual = answer_1(lines)
        self.assertEqual(expected, actual)

    def test_example_2(self):
        lines = EXAMPLE_INPUT.splitlines()
        expected = 24933642
        actual = answer_2(lines)
        self.assertEqual(expected, actual)

    def test_answer_1(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
        answer = answer_1(lines)
        print(f'\nAnswer 1 : {answer}\n')
        # expected =
        # self.assertEqual(expected, answer)

    def test_answer_2(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
        answer = answer_2(lines)
        print(f'\nAnswer 2 : {answer}\n')
        # expected =
        # self.assertEqual(expected, answer)

