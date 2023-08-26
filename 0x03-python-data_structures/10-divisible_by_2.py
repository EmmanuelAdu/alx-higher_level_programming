#!/usr/bin/python3
'''This function  finds all multiples of 2 in a list'''


def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    mul_2 = []
    for i in range(len(new_list)):
        if new_list[i] % 2 == 0:
            mul_2.append(True)
        else:
            mul_2.append(False)
    return (mul_2)
