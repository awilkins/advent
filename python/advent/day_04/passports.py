

from typing import Dict, List


OPTIONAL_FIELDS = ["cid"]

def check_int(value, lower, upper) -> bool:
    try:
        val: int = int(value)
        return lower <= val and val <= upper
    except:
        return False

def check_byr(value): return check_int(value, 1920,2002)

def check_iyr(value): return check_int(value, 2010, 2020)

def check_eyr(value): return check_int(value, 2020, 2030)

def check_hgt(value):
    units = value[-2:]

    if units == "cm":
        return check_int(value[:-2], 150, 193)

    if units == "in":
        return check_int(value[:-2], 59, 76)

    return False

def check_hcl(value):
    if len(value) != 7:
        return False

    if value[0] != '#':
        return False

    try:
        colour: int = int(value[1:], 16)
    except:
        return False

    return True


VALID_COLOURS = [ "amb", "blu", "brn", "gry", "grn", "hzl", "oth" ]
def check_ecl(value):
    return value in VALID_COLOURS


def check_pid(value):
    if len(value) != 9:
        return False

    for digit in value:
        if '0' > digit or digit > '9':
            return False

    return True

VALID_FIELDS = {
    "byr": check_byr,
    "iyr": check_iyr,
    "eyr": check_eyr,
    "hgt": check_hgt,
    "hcl": check_hcl,
    "ecl": check_ecl,
    "pid": check_pid,
}

def check_valid(passport: Dict[str, str], extended_validation=False):
    for field in VALID_FIELDS.keys():
        if field not in passport:
            return False

    if extended_validation:
       for field, check in VALID_FIELDS.items():
           if not check(passport[field]):
               return False

    return True

def parse(passports: List[str]):

    retval = []
    passport: Dict[str, str] = {}
    line = ""
    for line in passports:
        if len(line) == 0:
            retval.append(passport)
            passport = {}
            continue
        fields = line.split(' ')
        for field in fields:
            fieldname, value = field.split(':')
            passport[fieldname] = value

    if len(line):
        retval.append(passport)

    return retval


def check_passports(passports, extended=False):
    return [check_valid(passport, extended) for passport in parse(passports)]

