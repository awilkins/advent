from itertools import repeat
from typing import Dict, List

SIZE = 36

def make_mask(x: str, mask: str):
    m_trans = "01X"
    if x == "0":
        output = "100"
    else:
        output = "010"
    mask_str = mask.translate(
        str.maketrans(m_trans, output)
    )
    return int(mask_str, 2)

class BitComp:


    def __init__(self) -> None:
        self.memory: Dict[int, int] = {}
        self.set_mode(1)


    def set_mask(self, mask: str):
        assert(len(mask) == 36)

        mask = mask.zfill(SIZE)

        self.floating_positions = []
        for ii in range(SIZE):
            if mask[ii] == "X":
                self.floating_positions.append(ii)

        self.floating_count = sum([1 for c in mask if c == "X"])

        self.zeroes_mask = make_mask("0", mask)
        self.ones_mask = make_mask("1", mask)


    def maskval(self, value: int):
        bval = value

        # make a mask of zeroes - these zero bits out regardless (NOT)
        zval = bval & ~self.zeroes_mask
        # make a mask of ones - these set bits regardless (OR)
        oval = zval | self.ones_mask

        ival = oval
        return ival


    def poke(self, address: int, value: int) -> int:
        """ Poke value, returns actual value applied after mask """
        ival = self.maskval(value)
        self.memory[address] = ival
        return ival


    def splat(self, address: int, value: int) -> List[int]:
        """ returns the list of splatted addresses """

        masked_address = address | self.ones_mask

        float_high = 1 << self.floating_count

        addresses = []
        for floatbits in range(float_high):

            new_address = masked_address

            float_mask: int = 0
            inverse_float_mask: int = 0
            for ii in range(self.floating_count):
                bit = 2 ** ( (SIZE - 1) - self.floating_positions[ii])
                val = (floatbits >> (self.floating_count - ii - 1)) & 1
                float_mask |= val * bit
                inverse_float_mask |= (val ^ 1) * bit

            new_address &= ~inverse_float_mask # zeroes
            new_address |= float_mask # ones

            addresses.append(
                new_address
            )
        for addr in addresses:
            self.memory[addr] = value

        return addresses


    def checksum(self) -> int:
        return sum(self.memory.values())


    def set_mode(self, mode: int):
        if mode == 2:
            self.addr = self.splat
        else:
            self.addr = self.poke


    def load(self, program: List[str]):
        for line in program:
            instruction, value = line.split(' = ')

            if instruction == "mask":
                self.set_mask(value)
            else:
                address = int(instruction.split('[')[1][:-1])
                self.addr(address, int(value))





