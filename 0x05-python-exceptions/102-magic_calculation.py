#!/usr/bin/python3
'''This function performs exact function as the bytecode'''


def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result += (a ** b) / i
        except Exception as e:
            if str(e) == 'Too far':
                result += (a + b)
    return result
