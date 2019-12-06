
import unittest
from int_comp import run

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
