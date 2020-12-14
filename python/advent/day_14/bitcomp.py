from bitarray import bitarray
from itertools import repeat
from typing import Dict, List


class BitComp:


    def __init__(self) -> None:
        self.memory: Dict[int, int] = {}
        self.set_mode(1)


    def set_mask(self, mask: str):
        assert(len(mask) == 36)

        # 40 bits is easier 'cos you can't convert half a byte from an int
        mask = f"0000{mask}"

        def make_mask(x: str):
            m_trans = "01X"
            if x == "0":
                output = "100"
            else:
                output = "010"
            mask_str = mask.translate(
                str.maketrans(m_trans, output)
            )
            return bitarray(mask_str)

        self.mask = mask

        self.floating_positions = []
        for ii in range(40):
            if mask[ii] == "X":
                self.floating_positions.append(ii)

        self.floating_count = sum([1 for c in mask if c == "X"])

        self.zeroes_mask = make_mask("0")
        self.ones_mask = make_mask("1")


    def maskval(self, value: int):
        bval = bitarray(endian="big")
        bval.frombytes(value.to_bytes(5, byteorder="big"))

        # bval is _40_ bits not 36

        # make a mask of zeroes - these zero bits out regardless (NOT)
        zval = bval & ~self.zeroes_mask
        # make a mask of ones - these set bits regardless (OR)
        oval = zval | self.ones_mask

        ival = int.from_bytes(oval.tobytes(), "big")
        return ival


    def poke(self, address: int, value: int) -> int:
        """ Poke value, returns actual value applied after mask """
        ival = self.maskval(value)
        self.memory[address] = ival
        return ival


    def splat(self, address: int, value: int) -> List[int]:
        """ returns the list of splatted addresses """

        address_bits = bitarray()
        address_bits.frombytes(address.to_bytes(5, byteorder="big"))
        masked_address = address_bits | self.ones_mask

        float_high = 2 ** self.floating_count

        addresses = []
        for floatbits in range(float_high):
            bfloat = bin(floatbits)[2:].zfill(self.floating_count)
            new_address = masked_address.copy()
            for ii in range(len(bfloat)):
                new_address[self.floating_positions[ii]] = int(bfloat[ii], 2)
            addresses.append(
                int.from_bytes(new_address.tobytes(), "big")
            )
        for addr in addresses:
            try:
                self.memory[addr] = value
            except IndexError as e:
                print(addr, e)

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





