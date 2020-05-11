from typing import List
import time

class MagicIndex:
    def magic_index(self, x: List[int]) -> int:
        n = len(x) - 1
        start = 0
        end = n
        while start + 1 != end:
            i = self.half_index(start, end)
            if x[i] < i:
                start = i
            else:
                end = i  
        return end        

    def half_index(self, start: int, end: int) -> int:
        n = end - start + 1
        if n % 2:
            rest = int(n/2)
        else:
            rest = int(n/2 - 1)
        return start + rest