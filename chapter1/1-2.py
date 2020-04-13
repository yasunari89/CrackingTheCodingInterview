import sys
sys.path.append('./..')
from time_measure import time_measure
from tester import Tester


@time_measure(ndigits=10)
def check_permutation_by_sort(str1, str2):
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


@time_measure(ndigits=10)
def check_permutation_by_ascii_list(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        ascii_list = [0 for _ in range(128)]
        for letter in str1:
            ascii_list[ord(letter)] += 1
        for letter in str2:
            ascii_list[ord(letter)] -= 1
            if ascii_list[ord(letter)] < 0:
                return False
            else:
                pass 
        return True


if __name__ == "__main__":

    t = Tester()
    print(t.tell(check_permutation_by_sort('aab', 'aba'), True))
    print(t.tell(check_permutation_by_ascii_list('aab', 'aba'), True))
    print(t.tell(check_permutation_by_sort('aabc ', 'cab a'), True))
    print(t.tell(check_permutation_by_ascii_list('aabc ', 'cab a'), True))
    print(t.tell(check_permutation_by_sort('aaccb', 'abac'), False))
    print(t.tell(check_permutation_by_ascii_list('aaccb', 'abac'), False))
    print(t.tell(check_permutation_by_sort('aabgsss', 'sabsasu'), False))
    print(t.tell(check_permutation_by_ascii_list('aabgsss', 'sabsasu'), False))

    str1 = 'a' * 10000
    str2 = 'a' * 10000
    print(t.tell(check_permutation_by_sort(str1, str2), True))
    print(t.tell(check_permutation_by_ascii_list(str1, str2), True))
