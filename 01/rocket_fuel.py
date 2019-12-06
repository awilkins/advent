#/usr/bin/python3

import itertools
import math
import os
from functools import reduce

def add(one, two):
  return one + two

def fuel_for_mass(mass):
  return math.trunc(mass / 3.0) - 2

def fuel_for_fuel(mass):
  while mass > 0:
    mass = fuel_for_mass(mass)
    if mass < 0:
      mass = 0
    yield mass

def fuel_for_module(mass):
  return sum(fuel_for_fuel(mass)) 

mass_file = open("./rocket_modules.txt")
module_masses = [int(x) for x in mass_file.readlines()]
module_fuels = [fuel_for_module(mass) for mass in module_masses]

total_fuel = sum(module_fuels)

print("Total fuel", total_fuel)