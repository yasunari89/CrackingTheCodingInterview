class Bit:
    def get_bit(self, num: int, index: int) -> bool:
        return num & (num << index) != 0
    
    def set_bit(self, num: int, index: int) -> int:
        return num | (1 << index)
    
    def clear_bit(self, num: int, index: int) -> int:
        mask = -(1 << index)
        return num & mask 
    
    def clear_bits_from_top(self, num: int, index: int) -> int:
        mask = (1 << index) - 1
        return num & mask
    
    def clear_bits_from_bottom(self, num: int, index: int) -> int:
        mask = -1 << (index + 1)
        return num & mask
    
    def update_bit(self, num: int, index: int, bit_is_one: bool) -> int:
        value = 1 if bit_is_one else 0
        mask = ~(1 << index)
        return (num & mask) | (value << index)

    def float_to_bits(self, num: float):
        a = bin(int(num))[2:]
        few = num - int(num)
        b = []
        for _ in range(32-len(a)):
            few *= 2
            if few >= 1:
                b.append(1)
            else:
                b.append(0)
            few -= 1
        b = ''.join([str(e) for e in b])
        bit = float(a + '.' + b)
        return '0b' + str(bit)

