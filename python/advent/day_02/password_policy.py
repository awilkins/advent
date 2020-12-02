

from typing import Dict


def sled_policy(policy: str, password: str):

    span, charspec = policy.split(" ")
    pmin, pmax = [int(n) for n in span.split('-')]

    count = 0
    for char in password:

        if char == charspec:
            count += 1

        if count > pmax:
            return False

    if count < pmin:
        return False

    return True


def toboggan_policy(policy: str, password: str):
    span, charspec = policy.split(" ")
    pone, ptwo = [int(n) for n in span.split('-')]

    return (password[pone - 1] == charspec) != (password[ptwo - 1] == charspec)


def password_line_complies_with_policy(line: str, policy_filter=sled_policy):
    policy, password = line.split(': ')
    return policy_filter(policy, password)


def password_compliance_count(input: str, policy_filter=sled_policy):
    count = 0
    for line in [line for line in input.split('\n') if len(line) > 0]:
        if password_line_complies_with_policy(line, policy_filter):
            count += 1

    return count
