from __future__ import annotations

from typing import Sequence, List

class Pattern:

    field: List[List[str]]

    def __init__(self, lines):
        self.field = [
            list(line) for line in lines
        ]

    def rows(self):
        return self.field

    def columns(self):
        return [
            [line[xx] for line in self.field]
            for xx in range(len(self.field[0]))
        ]

    def is_vertical_reflection(self, xx):
        cols = self.columns()
        if xx > (len(self.field[0]) / 2):
            right_slice = cols[xx:]
            left_slice = cols[xx - len(right_slice):xx]
        else:
            left_slice = cols[0:xx]
            right_slice = cols[xx:xx + len(left_slice)]
        return right_slice[::-1] == left_slice
            
    def is_horizontal_reflection(self, yy):
        rows = self.rows()
        if yy > (len(self.field) / 2):
            top_slice = rows[yy:]
            bottom_slice = rows[yy - len(top_slice):yy]
        else:
            bottom_slice = rows[0:yy]
            top_slice = rows[yy:yy + len(bottom_slice)]
        return top_slice[::-1] == bottom_slice

    def find_reflection(self):
        vflec = 0
        hflec = 0
        for xx in range(1, len(self.field[0])):
            if self.is_vertical_reflection(xx):
                vflec = xx
        for yy in range(1, len(self.field)):
            if self.is_horizontal_reflection(yy):
                hflec = yy
            
        return vflec, hflec

    def find_other_reflection(self, other):
        vflec = 0
        hflec = 0
        for xx in range(1, len(self.field[0])):
            if other[0] != xx and self.is_vertical_reflection(xx):
                vflec = xx
        for yy in range(1, len(self.field)):
            if other[1] != yy and self.is_horizontal_reflection(yy):
                hflec = yy
            
        return vflec, hflec

            
def pattern_generator(lines: Sequence[str]):
    plines = []
    for line in lines:    
        if line == '':
            yield Pattern(plines)
            plines = []
        else:
            plines.append(line)
    if len(plines):
        yield Pattern(plines)

def answer_1(lines: Sequence[str]):
    pg = pattern_generator(lines)

    vt = 0
    ht = 0 
    for p in pg:
        v, h = p.find_reflection()
        vt += v
        ht += h
    
    return (ht * 100) + vt

def get_new_reflection(p: Pattern):
    orig = p.find_reflection()
    for yy in range(len(p.field)):
        for xx in range(len(p.field[0])):
            c = p.field[yy][xx]
            p.field[yy][xx] = '#' if c == '.' else '.'
            new = p.find_other_reflection(orig)
            p.field[yy][xx] = c
            if new != (0, 0):
                return new
    
def answer_2(lines: Sequence[str]):
    pg = pattern_generator(lines)
    
    vt = 0
    ht = 0

    for p in pg:
        v, h = get_new_reflection(p)
        vt += v
        ht += h
    
    return (ht * 100) + vt


