#!/usr/bin/python3
'''This function replace all occurrence of an elemt by another in new list'''


def search_replace(my_list, search, replace):
    new_list = []
    for a in my_list:
        if a == search:
            new_list.append(replace)
        else:
            new_list.append(a)
    return (new_list)
