from __future__ import annotations

from ctypes import c_uint16

from typing import Sequence


def op_or(a, b=0):
    return a | b

def op_and(a, b):
    return a & b

def op_lshift(a, b):
    return a << b

def op_rshift(a, b):
    return a >> b

def op_not(a, b):
    return ~ b

OPS = {
    'AND': op_and,
    'LSHIFT': op_lshift,
    'RSHIFT': op_rshift,
    'OR': op_or,
}

def answer_1(lines: Sequence[str], outputs=None):

    outputs = outputs or {}

    while len(outputs) < len(lines):
        for line in lines:
            parts = line.split('->')
            out_key = parts[1].strip()

            if out_key in outputs:
                continue

            parts = parts[0].split()

            a = '0'
            b = '0'
            op = op_or

            if len(parts) > 2:
                a = parts[0]
                b = parts[2]
                op = OPS[parts[1]]
            elif len(parts) == 2:
                b = parts[1]
                op = op_not
            else:
                a = parts[0]


            if not a[0].isdigit():
                if not a in outputs:
                    continue
                a = outputs[a]

            if not b[0].isdigit():
                if not b in outputs:
                    continue
                b = outputs[b]

            a = int(a)
            b = int(b)
            output = op(a, b)
            # Clip output to what a 16 bit unsigned int can represent
            output = c_uint16(output).value
            outputs[out_key] = output

    return outputs


def answer_2(lines: Sequence[str]):
    outputs = answer_1(lines, {})
    return answer_1(lines, dict(b = outputs['a']))

