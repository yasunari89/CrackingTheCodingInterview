class TripleStep:
    def __init__(self, max_size=100):
        self.max_size = max_size
        self.memo = [None for _ in range(max_size)]
    
    def step(self, steps):
        if steps > self.max_size:
            raise Exception('RAISE THE MEMO SIZE')
        if steps < 0:
            return 0
        elif steps == 0:
            return 1
        else:
            if not self.memo[steps-1]:
                self.memo[steps-1] = self.step(steps-1) + self.step(steps-2) + self.step(steps-3)
            return self.memo[steps-1]