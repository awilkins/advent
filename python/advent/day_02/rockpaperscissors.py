

SCORES = dict(
    A=1,
    B=2,
    C=3,
)

#        R    P    S
ELF = [ 'A', 'B', 'C' ]
YOU = [ 'X', 'Y', 'Z' ]

def score(elf, you):
    i_you = YOU.index(you)
    i_elf = ELF.index(elf)

    score = 0

    if i_you == i_elf:
        score = 3

    if i_you - i_elf == 1 or i_you - i_elf == -2:
        score = 6

    score += i_you + 1

    return score

def score_2(elf, outcome):
    i_outcome = YOU.index(outcome) - 1
    i_elf = ELF.index(elf)

    i_response = i_elf + i_outcome
    i_response %= 3
    response = YOU[i_response]
    return score(elf, response)


def answer_1(lines):
    total = 0

    for line in lines:
        elf, you = line.split(' ')
        total += score(elf, you)

    return total

def answer_2(lines):
    total = 0

    for line in lines:
        elf, you = line.split(' ')
        total += score_2(elf, you)

    return total
