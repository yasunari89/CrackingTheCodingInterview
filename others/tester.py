class Tester:
    def __init__(self):
        self.n = 0
        self.result = None
        self.answer = None

    def test(self):
        self.n += 1
        if self.result == self.answer:
            return True 
        else:
            return False 

    def tell(self, result, answer):
        self.result = result
        self.answer = answer
        remarks = {True: 'Completed.', False: 'Failed.'}
        test_result = self.test()
        return 'TEST {}: {}'.format(self.n, remarks[test_result])
