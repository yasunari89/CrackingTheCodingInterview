from typing import List

class NextNumber:
    def __init__(self, num: int):
        self.num = bin(num)[2:]

    def larger(self) -> str:
        zero_index = self.find_continuous_zero_to_tail()
        zero_index = zero_index if zero_index != None else len(self.num)
        one_index = self.find_continuous_one_to_zero(zero_index)
        larger_num = [s for s in self.num]
        n = len(larger_num)
        for i in range(n-(zero_index-one_index)+1, n):
            larger_num[i] = '1'
        for i in range(one_index, one_index+n-zero_index+1):
            larger_num[i] = '0'
        if one_index < 0:
            larger_num.insert(0, '1')
        else:
            larger_num[one_index-1] = '1'
        return ''.join(larger_num)
    
    def find_continuous_zero_to_tail(self):
        reversed_num = reversed(self.num)
        index = len(self.num)
        for i, v in enumerate(reversed_num):
            v = int(v)
            if i == 0 and v == 1:
                return None 
            else:
                if v == 0:
                    index -= 1
                else:
                    return index
                                
    def find_continuous_one_to_zero(self, zero_index):
        i = zero_index - 1
        while i >= 0:
            if self.num[i] == '0':
                return i + 1
            i -= 1
        return 0
