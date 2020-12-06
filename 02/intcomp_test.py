
import unittest

import queue

from intcomp import run, execute

class TestPrograms(unittest.TestCase):

  def test_one(self):
    output, memory = run("1,0,0,0,99")
    self.assertEqual(2, output)

  def test_two(self):
    output, memory = run("2,3,0,3,99")
    self.assertEqual(6, memory[-2])


  def test_three(self):
    output, memory = run("2,4,4,5,99,0")
    expected = 9801
    self.assertEqual(expected, memory[-1])

  def test_four(self):
    output, memory = run("1,1,1,4,99,5,6,0,99")
    expected = [30, 1, 1, 4, 2, 5, 6, 0, 99]
    self.assertEqual(memory, expected)

  def test_five(self):
    output, memory = run("1,9,10,3,2,3,11,0,99,30,40,50")
    expected = [3500, 9, 10, 70,
               2, 3, 11, 0,
               99,
               30, 40, 50]
    self.assertEqual(memory, expected)

  def test_v2(self):
    input = queue.Queue()
    output = queue.Queue()

    expected = 69
    input.put(expected)

    memory = [3, 0, 4, 0, 99]
    result, memory = execute(memory, input, output)

    actual = output.get()
    self.assertEqual(expected, actual)

  def test_immediate(self):
    program = [1002, 4, 3, 4, 33]
    expected = [1002, 4, 3, 4, 99]

    result, memory = execute(program)
    self.assertEqual(expected, memory)

  def test_negs(self):
    program = [1101, 100, -1, 4, 0]
    expected = [1101, 100, -1, 4, 99]

    result, memory = execute(program)
    self.assertEqual(expected, memory)

  def test_jmt(self):
    program = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]

    stdin = queue.Queue()
    stdout = queue.Queue()

    # test true
    stdin.put(8)

    exitcode, memory = execute(program, stdin, stdout)
    result = stdout.get()
    self.assertEqual(1, result)

