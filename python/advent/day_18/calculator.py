

from typing import List, Union

from itertools import repeat


def evaluate(line: Union[str, List[Union[int, str]]]) -> int:

    val = 0
    op = "+"

    ii = 0
    while ii < len(line):

        c = line[ii]

        if c == " ":
            ii += 1
            continue

        if c == "+" or c == "*":
            op = c
            ii += 1
            continue

        if c == "(":
            open_braces = 1
            bb = ii + 1
            # look forward for matching brace
            while open_braces > 0:
                c = line[bb]

                if c == "(":
                    open_braces += 1

                if c == ")":
                    open_braces -= 1

                bb += 1
            # evaluate subexpression
            subexpression = line[ii + 1 : bb - 1]
            c = str(evaluate(subexpression))
            # reset index
            ii = bb

        operand: int = int(c)

        if op == "+":
            val += operand

        if op == "*":
            val *= operand

        ii += 1

    return val


def maffs_2(line):

    terms = list(line)

    while '+' in terms:
        ii = 0
        last_numeric = -1
        last_op = 0
        while ii < len(terms):

            t = terms[ii]

            if t == " ":
                ii += 1
                continue

            if t == "+":
                last_op = ii
                ii += 1
                continue

            if t == "(":
                open_braces = 1
                bb = ii + 1
                # look forward for matching brace
                while open_braces > 0:
                    c = line[bb]

                    if c == "(":
                        open_braces += 1

                    if c == ")":
                        open_braces -= 1

                    bb += 1
                # evaluate subexpression
                subexpression = terms[ii + 1 : bb - 1]
                replacement: List[Union[int, str]] = [
                    " ",
                    maffs_2("".join(str(t) for t in subexpression)),
                    " ",
                ]
                replacement.extend(repeat(" ", len(subexpression) - 1))
                tlen = len(terms)
                terms[ii:bb] = replacement
                assert len(terms) == tlen
                break


            if (type(t) is int or ('0' <= t and t <= '9')):
                if last_numeric >= 0 and last_op > 0:
                    subexpression = terms[last_numeric : ii + 1]
                    terms[last_op] = evaluate(subexpression)
                    terms[last_numeric] = " "
                    terms[ii] = " "
                    break
                last_numeric = ii

            ii += 1

    return evaluate(terms)








