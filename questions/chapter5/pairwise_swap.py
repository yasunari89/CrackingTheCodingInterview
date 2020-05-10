class PairwiseSwap:
    def swap(self, num: int) -> int:
        bin_num = bin(num)[2:]
        n = len(bin_num)
        if n % 2 != 0:
            num -= 2**(n-1)
            mask1 = ''.join(['10' for _ in range(int((n-1)/2))])
            mask2 = ''.join(['01' for _ in range(int((n-1)/2))])
            return 2**(n-1) + (((num & int(mask1, 2)) >> 1) | ((num & int(mask2, 2)) << 1))
        else:
            mask1 = ''.join(['10' for _ in range(int(n/2))])
            mask2 = ''.join(['01' for _ in range(int(n/2))])
            return ((num & int(mask1, 2)) >> 1) | ((num & int(mask2, 2)) << 1)
