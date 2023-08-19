#!/usr/bin/python3
'''This function returns a list with all values mul by a num'''


def multiply_list_map(my_list=[], number=0):
    mul_list = map(lambda x: x * number, my_list)
    return (list(mul_list))
