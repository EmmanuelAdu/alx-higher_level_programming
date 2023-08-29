#!/usr/bin/python3
'''This function divides two int and prints the results'''


def safe_print_division(a, b):
    try:
        result = a / b
    except (ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
