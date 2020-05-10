from typing import List

class NextNumber:
    def __init__(self, num: int):
        self.num = num
        self.bin_num = bin(num)[2:]

    def larger(self) -> str:
        c0 = self.count_last_zeros(len(self.bin_num)-1)
        c1 = self.count_last_ones(len(self.bin_num)-c0-1)
        return self.num + (1 << c0) + (1 << (c1 - 1)) - 1

    def count_last_zeros(self, last_index):
        counter = 0
        index = last_index
        while index >= 0:
            if self.bin_num[index] == '1':
                return counter
            else:
                counter += 1
                index -= 1
        return counter
    
    def count_last_ones(self, last_index):
        counter = 0
        index = last_index
        while index >= 0:
            if self.bin_num[index] == '0':
                return counter
            else:
                counter += 1
                index -= 1
        return counter
    
