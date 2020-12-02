from unittest import TestCase

from ..util import get_resource

from advent.day_02.password_policy import \
    sled_policy, \
    toboggan_policy, \
    password_line_complies_with_policy, \
    password_compliance_count

EXAMPLE_INPUT = """\
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc\
"""


class Day02Tests(TestCase):

    def test_good_password(self):
        self.assertTrue(sled_policy('1-3 a', 'abcde'))
        self.assertTrue(sled_policy('2-9 c', 'ccccccccc'))

    def test_bad_password(self):
        self.assertFalse(sled_policy('1-3 b', 'cdefg'))

    def test_plines(self):
        lines = EXAMPLE_INPUT.split('\n')

        self.assertTrue(password_line_complies_with_policy(lines[0]))
        self.assertFalse(password_line_complies_with_policy(lines[1]))
        self.assertTrue(password_line_complies_with_policy(lines[2]))

    def test_count_compliance(self):
        self.assertEqual(2, password_compliance_count(EXAMPLE_INPUT))

    def test_answer_1(self):
        passwords = get_resource('day_02/input.txt').read_text()
        print(f'\nDay 02 Answer 01 : {password_compliance_count(passwords)}')

    def test_toboggan_policy(self):
        lines = EXAMPLE_INPUT.split('\n')

        self.assertTrue(password_line_complies_with_policy(
            lines[0], policy_filter=toboggan_policy))
        self.assertFalse(password_line_complies_with_policy(
            lines[1], policy_filter=toboggan_policy))
        self.assertFalse(password_line_complies_with_policy(
            lines[2], policy_filter=toboggan_policy))

    def test_answer_2(self):
        passwords = get_resource('day_02/input.txt').read_text()
        print(
            f'\nDay 02 Answer 02 : {password_compliance_count(passwords, toboggan_policy)}')
