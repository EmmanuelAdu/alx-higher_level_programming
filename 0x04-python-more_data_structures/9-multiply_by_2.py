#!/usr/bin/python3
'''This function returns a new dictionary with all values multiplied by 2'''


def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    my_keys = new_dict.keys()
    for i in my_keys:
        new_dict[i] *= 2
    return (new_dict)
