import sys 
from tester import Tester
from time_measure import time_measure


def find_blanks(string, true_length):
    blank_indexes = []
    for i in range(true_length):
        if string[i] == '':
            blank_indexes.append(i)
    return blank_indexes


def replace_to_20(string, indexes):
    r_indexes = [indexes[i] for i in range(len(indexes, 0, -1))]
    for i in r_indexes:
        temp = string[i+1:]
        string[i] = '%20'
        string = string + temp
    return string


def URLify(string, true_length):
    return replace_to_20(string, find_blanks(string, true_length))