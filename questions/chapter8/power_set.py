class PowerSet:
    def __init__(self, size=100):
        self.memo = [None for _ in range(size)]

    def count(self, set_num):
        if set_num == 0:
            return 1
        else:
            if not self.memo[set_num]:
                self.memo[set_num] = 2 * self.count(set_num-1)
            return self.memo[set_num]