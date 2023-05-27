#!/usr/bin/python3

from unittest import TestCase
from ..util import get_resource

DAY="01"
from advent.day_01.rocket_fuel import *


class TestFuelCalculations(TestCase):

    @classmethod
    def setup_class(cls):
        cls.input = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()

    def test_twelve(self):
        self.assertEqual(2, fuel_for_mass(12))

    def test_fourteen(self):
        self.assertEqual(2, fuel_for_mass(14))


    def test_nice(self):
        self.assertEqual(654, fuel_for_mass(1969))

    def test_loads(self):
        self.assertEqual(33583, fuel_for_mass(100756))

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




class TestComplexFuelCalculations(TestCase):
    def test_twelve(self):
        self.assertEqual(2, fuel_for_module(12))

    def test_nice(self):
        self.assertEqual(966, fuel_for_module(1969))
