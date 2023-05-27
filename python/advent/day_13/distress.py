
import operator
from typing import List


def gen_groups(lines):
    group = []

    for line in lines:
        if len(line):
            group.append(line)
        else:
            yield group
            group = []

    yield group


class Packet:

    val: List[int|List]


    def __init__(self, line):
        self.val = eval(line)


    def __lt__(self, other):

        this = self.val
        othe = other.val

        return self.lt(this, othe)

    def __eq__(self, __o: "Packet") -> bool:
        this = self.val
        othe = __o.val
        return self.eq(this, othe)

    def __gt__(self, __o) -> bool:
        this = self.val
        othe = __o.val
        return self.lt(othe, this)

    def __ge__(self, __o):
        return self.__eq__(__o) or self.__gt__(__o)

    def __le__(self, __o):
        return self.__eq__(__o) or self.__lt__(__o)

    def __ne__(self, __o):
        return not self.__eq__(__o)

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


    def lt(self, this, othe):

        if type(this) != type(othe):
            if type(this) == int: this = [this]
            if type(othe) == int: othe = [othe]
        elif type(this) == int and this != othe:
            return this < othe
        elif type(this) == int:
            return False

        for ix, item in enumerate(this):
            sub_this = item
            if len(othe) <= ix:
                return False
            sub_othe = othe[ix]
            if not self.eq(sub_this, sub_othe):
                return self.lt(sub_this, sub_othe)

        return len(this) < len(othe)


    def eq(self, this, othe):

        if type(this) != type(othe):
            if type(this) == int: this = [this]
            if type(othe) == int: othe = [othe]
        elif type(this) == int:
            return this == othe

        if len(this) != len(othe):
            return False

        for ix, item in enumerate(this):
            sub_this = item
            sub_othe = othe[ix]
            if not self.eq(sub_this, sub_othe):
                return False

        return True



def answer_1(lines: List[str]):
    groups = gen_groups(lines)

    total = 0

    for ix, group in enumerate(groups):
        if Packet(group[0]) < Packet(group[1]):
            total += ix + 1

    return total


def answer_2(lines: List[str]):
    packets = list(Packet(line) for line in lines if len(line) > 0)

    divider_2 = Packet("[[2]]")
    divider_6 = Packet("[[6]]")
    packets.append(divider_2)
    packets.append(divider_6)

    sorted_packets = sorted(packets)

    print()
    print("\n".join(str(packet) for packet in sorted_packets))

    ix_2 = sorted_packets.index(divider_2) + 1
    ix_6 = sorted_packets.index(divider_6) + 1

    return ix_2 * ix_6

