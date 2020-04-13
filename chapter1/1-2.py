def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        s1 = sorted(str1)
        s2 = sorted(str2)
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            else:
                return False
        return True


if __name__ == "__main__":
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
            remarks = {True: 'OK!', False: 'Failed.'}
            test_result = self.test()
            return 'TEST {}: {}'.format(self.n, remarks[test_result])

    t = Tester()
    print(t.tell(check_permutation('aab', 'aba'), True))
    print(t.tell(check_permutation('aabc ', 'cab a'), True))
    print(t.tell(check_permutation('aaccb', 'abac'), False))
    print(t.tell(check_permutation('aabgsss', 'sabsasu'), False))
