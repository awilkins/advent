from unittest import TestCase

from ..util import get_resource
from advent.day_04.passports import check_passports

EXAMPLE_INPUT="""\
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

class TestPassports(TestCase):

    def test_example(self):
        self.assertEqual(
            [True, False, True, False],
            check_passports(EXAMPLE_INPUT.splitlines()),
        )
        self.assertEqual(2, sum(check_passports(EXAMPLE_INPUT.splitlines())))


    def test_answer_1(self):
        passports = get_resource('day_04/input.txt').read_text().splitlines()
        print(f'Answer 01 : {sum(check_passports(passports))}')

    def test_answer_2(self):
        passports = get_resource('day_04/input.txt').read_text().splitlines()
        print(f'Answer 02 : {sum(check_passports(passports, extended=True))}')


