import os
from pathlib import Path
from unittest import TestCase

from ..util import get_resource

from advent.day_01.advent_01 import expense_anomaly, expense_anomaly_triple


class Advent01Tests(TestCase):
    def test_example(self):
        expenses = '''\
1721
979
366
299
675
1456
'''

        answer = 514579

        self.assertEqual(answer, expense_anomaly(expenses))

    def test_problem(self):

        expense_path = get_resource('day_01/input_01.txt')
        expenses = open(expense_path).read()

        print('\nAnswer 1:')
        print(expense_anomaly(expenses))
        print('Answer 2:')
        print(expense_anomaly_triple(expenses))
        print()
