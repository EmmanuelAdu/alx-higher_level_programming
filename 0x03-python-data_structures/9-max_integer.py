#!/usr/bin/python3
'''This function returns the maximum value of a list'''


def max_integer(my_list=[]):
    if my_list == "":
        return None
    max_val = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > max_val:
            max_val = my_list[i]
    return max_val
