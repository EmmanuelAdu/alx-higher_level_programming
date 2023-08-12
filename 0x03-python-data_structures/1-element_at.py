#!/usr/bin/python3
'''This function retrieves an element from a list like in c'''


def element_at(my_list, idx):
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    return (my_list[idx])
