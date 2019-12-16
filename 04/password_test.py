import unittest

from password import check

class TestPassword(unittest.TestCase):

  def test_all_ones(self):
    self.assertTrue(check("111111"))

  def test_descending(self):
    self.assertFalse(check("223450"))

  def test_no_double(self):
    self.assertFalse(check("123789"))