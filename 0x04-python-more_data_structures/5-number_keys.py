#!/usr/bin/python3
'''This function returns the number of keys in a dictionary'''


def number_keys(a_dictionary):
    total_num = 0
    total_keys = list(a_dictionary.keys())
    for i in total_keys:
        total_num += 1
    return (total_num)
