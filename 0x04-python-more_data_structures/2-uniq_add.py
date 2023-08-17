#!/usr/bin/python3
'''This function adds all unique integers in a list(only once for each)'''


def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    add = 0
    for a in uniq_list:
        add += a
    return (add)
