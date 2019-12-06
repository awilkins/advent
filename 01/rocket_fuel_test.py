#!/usr/bin/python3

import unittest
from rocket_fuel import fuel_for_module, fuel_for_mass

class TestFuelCalculations(unittest.TestCase):

  def test_twelve(self):
    self.assertEqual(2, fuel_for_mass(12))
  
  def test_fourteen(self):
    self.assertEqual(2, fuel_for_mass(14))


  def test_nice(self):
    self.assertEquals(654, fuel_for_mass(1969))

  def test_loads(self):
    self.assertEqual(33583, fuel_for_mass(100756))

class TestComplexFuelCalculations(unittest.TestCase):
  def test_twelve(self):
    self.assertEqual(2, fuel_for_module(12))
  
  def test_nice(self):
    self.assertEqual(966, fuel_for_module(1969))